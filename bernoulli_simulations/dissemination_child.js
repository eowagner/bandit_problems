var slot_machines = require('./bandit_utils/slot_machines.js');
var beta_agents = require('./bandit_utils/agents.js');
var social_networks = require('./bandit_utils/social_networks.js');

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

	for (var r=0; r<parameters.runs; r++) {
		// Flip coin to determine order of machines and thus which machine is censored
		var target = 1;
		var network;

		if (parameters.p[0] > parameters.p[1]) {
			target = 0;
		}

		if (Math.random() < .5) {
			network = new social_networks.DisseminationDummyNetwork(agent_list, machine_list, parameters.graphs);
		}
		else {
			network = new social_networks.DisseminationDummyNetwork(agent_list, machine_list_flipped, parameters.graphs);
			target = (target==1) ? 0 : 1;
		}


		agent_list.forEach(function (a) {
			a.reset();
		});

		for (var t=0; t<parameters.steps; t++) {
			network.step();
		}

		if (network.hasDummyLearned(target))
			success_count++;

		if (network.hasReachedConsensus())
			consensus_count++;
	}

	return {
		parameters: parameters,
		success_count: success_count,
		consensus_count: consensus_count
	};
}


process.on('message', function(message) {
	var sim_results = simulate(message);

	process.send(sim_results);

	process.disconnect();
});