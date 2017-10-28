var slot_machines = require('../bandit_utils/slot_machines.js');
var beta_agents = require('../bandit_utils/agents.js');
var social_networks = require('../bandit_utils/social_networks.js');
var argv = require('minimist')(process.argv.slice(2));

var runs = 10;
var steps = 1000;
var priors = "uniform";
var q = .6;
var which_arm_restricted = "randomize"; //low, or high
var num_agents = 9;

if ('p' in argv)
	priors = argv['p'];

if ('r' in argv)
	runs = argv['r'];

if ('s' in argv)
	steps = argv['s'];

if ('n' in argv)
	num_agents = argv['n'];

if ('c' in argv)
	which_arm_restricted = argv['c'];

if ('q' in argv)
	q = argv['q'];

console.log("# Priors: " + priors + "; runs: " + runs + "; steps: " + steps);
console.log("# Which arm is restricted: " + which_arm_restricted);
console.log("index,diss_success_time,diss_incorrect_time,complete_success_time,complete_incorrect_time");

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

	var network = new social_networks.DisseminationDummyNetwork(agent_list, machine_list, parameters.graphs);

	var successful_lock_times = [];
	var incorrect_lock_times = [];

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

		var last_choice = dummy_choices.shift();
		// var time_to_lock = dummy_choices.findIndex((x) => {return x!=last_choice} );
		var flipped = (last_choice==0) ? 1 : 0;
		var time_to_lock = dummy_choices.indexOf(flipped);

		if (time_to_lock == -1)
			time_to_lock = 0;
		else
			time_to_lock = parameters.steps - time_to_lock + 1; //The last choice was removed with the shift

		if (last_choice==target)
			successful_lock_times.push(time_to_lock);
		else
			incorrect_lock_times.push(time_to_lock);
	}

	return {
		successful_lock_times: successful_lock_times,
		incorrect_lock_times: incorrect_lock_times
	};
}

var start_time = new Date().getTime();

var complete_graph = social_networks.makeCompleteGraph(num_agents);
var star_graph = social_networks.makeStarGraph(num_agents);

var randomize = (which_arm_restricted=="randomize") ? true : false;
if (which_arm_restricted=="low")
	graph_list = [star_graph, complete_graph];

var parameters = {
	priors: priors,
	p: [.5, q],
	runs: runs,
	steps: steps,
	randomize: randomize,
	graphs: [complete_graph, star_graph]
};

var results_diss_restricted = simulate(parameters);

var parameters = {
	priors: priors,
	p: [.5, q],
	runs: runs,
	steps: steps,
	randomize: randomize,
	graphs: [complete_graph, complete_graph]
};

var results_complete = simulate(parameters);

var lengths = [results_diss_restricted.successful_lock_times.length, results_diss_restricted.incorrect_lock_times.length, results_complete.successful_lock_times.length, results_complete.incorrect_lock_times.length ];
var m = Math.max.apply(null, lengths);

for (var i=0; i<m; i++) {
	var s = i + ",";
	
	if (i<results_diss_restricted.successful_lock_times.length)
		s += results_diss_restricted.successful_lock_times[i];
	s += ",";

	if (i<results_diss_restricted.incorrect_lock_times.length)
		s += results_diss_restricted.incorrect_lock_times[i];
	s += ",";

	if (i<results_complete.successful_lock_times.length)
		s += results_complete.successful_lock_times[i];
	s += ",";

	if (i<results_complete.incorrect_lock_times.length)
		s += results_complete.incorrect_lock_times[i];
	
	console.log(s);
}

var end_time = new Date().getTime();
console.log("# " + (end_time-start_time)/1000/60 + " minutes elapsed");
