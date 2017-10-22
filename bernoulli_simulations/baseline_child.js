var slot_machines = require('../bandit_utils/slot_machines.js');
var beta_agents = require('../bandit_utils/agents.js');
var social_networks = require('../bandit_utils/social_networks.js');

function simulate(parameters) {
	var machine_list = [];
	for (var i=0; i<parameters.p.length; i++) {
		machine_list.push(new slot_machines.BernoulliMachine(parameters.p[i]));
	}

	var agent_list = [];
	for (var i=0; i<parameters.graphs[0].length; i++) {
		switch (parameters.priors) {
			case "uniform":
			case "u":
				// agent_list.push(new beta_agents.BetaAgent(machine_list.length));
				agent_list.push(new beta_agents.BetaAgentUniformPriors(machine_list.length));
				break;
			case "jeffrey":
			case "j":
				agent_list.push(new beta_agents.BetaAgentJeffreyPriors(machine_list.length))
				break;
			case "random":
			case "r":
				agent_list.push(new beta_agents.BetaAgentRandomPriors(machine_list.length));
				break;
			default:
				agent_list.push(new beta_agents.BetaAgentUniformPriors(machine_list.length));
		}
		
	}

	var networks = [];
	for (var i=0; i<parameters.graphs.length; i++) {
		networks[i] = new social_networks.DummyNetwork(agent_list, machine_list, parameters.graphs[i]);
	}

	// My office computer has an outdated version of node lacking fill
	// var success_counts = new Array(networks.length).fill(0);
	// var consensus_counts = new Array(networks.length).fill(0);
	var success_counts = [];
	var consensus_counts = [];
	var total_times_to_lock = [];

	for (var net_index=0; net_index<networks.length; net_index++) {
		success_counts.push(0);
		consensus_counts.push(0);
		total_times_to_lock.push(0);

		for (var r=0; r<parameters.runs; r++) {
			agent_list.forEach(function (a) {
				a.reset();
			});

			var dummy_choices = [];
			for (var t=0; t<parameters.steps; t++) {

				dummy_choices.unshift(networks[net_index].getDummyChoice());

				networks[net_index].step();
			}

			var last_choice = dummy_choices.shift();
			var time_to_lock = dummy_choices.findIndex((x) => {return x!=last_choice} );
			time_to_lock = parameters.steps - 1 - time_to_lock; //The last choice was removed with the shift
			total_times_to_lock[net_index] += time_to_lock;

			if (networks[net_index].hasDummyLearned(parameters.target))
				success_counts[net_index]++;

			if (networks[net_index].hasReachedConsensus())
				consensus_counts[net_index]++;
		}
	}

	return {
		parameters: parameters,
		success_counts: success_counts,
		consensus_counts: consensus_counts,
		total_times_to_lock: total_times_to_lock 
	};
}


process.on('message', function(message) {
	var sim_results = simulate(message);

	process.send(sim_results);

	process.disconnect();
});