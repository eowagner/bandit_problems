var slot_machines = require('./bandit_utils/slot_machines.js');
var beta_agents = require('./bandit_utils/beta_agents.js');
var social_networks = require('./bandit_utils/social_networks.js');

function simulate(parameters) {
	var num_agents = parameters.num_agents;

	var agent_list = new Array(num_agents);
		for (var i=0; i<num_agents; i++) {
		agent_list[i] = new beta_agents.BetaAgent(2);
	}

	var completeGraph = social_networks.makeCompleteGraph(agent_list.length);
	// var cycleGraph = social_networks.makeCycleGraph(agent_list.length);
	var starGraph = social_networks.makeStarGraph(agent_list.length);

	var p_list = [];
	var succ_complete = [];
	var succ_star = [];
	var index = 0;

	for (var p=.505; p<=.7; p+=.005) {
		p_list.push(p);
		succ_complete.push(0);
		succ_star.push(0);

		var machine_list = [new slot_machines.BernoulliMachine(.5), new slot_machines.BernoulliMachine(p)];
		var netComplete = new social_networks.DummyNetwork(agent_list, machine_list, completeGraph);
		var netStar = new social_networks.DummyNetwork(agent_list, machine_list, starGraph);

		for (var r=0; r<parameters.runs; r++) {
			agent_list.forEach(function(a) {
				if (parameters.priors_index==0)
					a.resetUniformPriors();
				else if (parameters.priors_index==1)
					a.resetJeffreyPriors();
				else 
					a.resetRandomInterval([0,4], [0,4]);
			});

			for (var t=0; t<parameters.steps; t++) {
				netComplete.step();
			}

			if (netComplete.hasDummyLearned(1))
				succ_complete[index]++;
		}

		for (var r=0; r<parameters.runs; r++) {
			agent_list.forEach(function(a) {
				a.resetUniformPriors();
			});

			for (var t=0; t<parameters.steps; t++) {
				netStar.step();
			}

			if (netStar.hasDummyLearned(1))
				succ_star[index]++;
		}

		console.log(parameters.priors_index + ", " + p + ": " + succ_complete[index] + ", " + succ_star[index]);
		index++;
	}

	return {
		p_list: p_list,
		succ_complete: succ_complete,
		succ_star: succ_star
	};
}

process.on('message', function(message) {
	
	var sim_results = simulate(message);

	process.send( { 
		priors_index: message.priors_index,
		sim_results: sim_results
	});

	process.disconnect();
});