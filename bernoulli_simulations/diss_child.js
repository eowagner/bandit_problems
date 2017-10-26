var slot_machines = require('../bandit_utils/slot_machines.js');
var beta_agents = require('../bandit_utils/agents.js');
var social_networks = require('../bandit_utils/social_networks.js');

function simulate(parameters) {
	var machine_list = [];
	for (var i=0; i<parameters.p.length; i++) {
		machine_list.push(new slot_machines.BernoulliMachine(parameters.p[i]));
	}

	var machine_list_flipped = [];
	for (var i=parameters.p.length-1; i>=0; i--) {
		machine_list_flipped.push(new slot_machines.BernoulliMachine(parameters.p[i]));
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

	// This works a little differently than the baseline child.  Rather than running multiple networks, this runs a single network
	// And the array of graphs is just the dissemination network for each arm.
	var network = new social_networks.DisseminationDummyNetwork(agent_list, machine_list, parameters.graphs);

	var success_count = 0;
	var consensus_count = 0;
	var total_time_to_lock = 0;
	var total_time_to_successful_lock = 0;
	var total_time_to_incorrect_lock = 0;

	for (var r=0; r<parameters.runs; r++) {
		var target = (parameters.p[0] > parameters.p[1]) ? 0 : 1;
		var network = new social_networks.DisseminationDummyNetwork(agent_list, machine_list, parameters.graphs);

		if (parameters.randomize == true) {
		// Flip coin to determine order of machines and thus which machine is censored
			if (Math.random() < .5) {
				network = new social_networks.DisseminationDummyNetwork(agent_list, machine_list_flipped, parameters.graphs);
				target = (target==1) ? 0 : 1;
			}
		}

		agent_list.forEach(function (a) {
			a.reset();
		});

		var dummy_choices = [];
		for (var t=0; t<parameters.steps; t++) {
			network.step();
			dummy_choices.unshift(network.getDummyChoice());
		}

		if (network.hasDummyLearned(target))
			success_count++;

		if (network.hasReachedConsensus())
			consensus_count++;

		var last_choice = dummy_choices.shift();
		var time_to_lock = dummy_choices.findIndex((x) => {return x!=last_choice} );
		if (time_to_lock == -1)
			time_to_lock = 0;
		else
			time_to_lock = parameters.steps - 1 - time_to_lock; //The last choice was removed with the shift
		total_time_to_lock += time_to_lock;

		if (last_choice==target)
			total_time_to_successful_lock += time_to_lock;
		else
			total_time_to_incorrect_lock += time_to_lock;
	}

	return {
		parameters: parameters,
		success_count: success_count,
		consensus_count: consensus_count,
		total_time_to_lock: total_time_to_lock,
		total_time_to_successful_lock: total_time_to_successful_lock,
		total_time_to_incorrect_lock: total_time_to_incorrect_lock
	};
}


process.on('message', function(message) {
	var sim_results = simulate(message);

	process.send(sim_results);

	process.disconnect();
});