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

var ps = [.5, q];

var complete_graph = social_networks.makeCompleteGraph(num_agents);
var star_graph = social_networks.makeStarGraph(num_agents);

var randomize = (which_arm_restricted=="randomize") ? true : false;
var graph_list = [complete_graph, star_graph];
if (which_arm_restricted=="low")
	graph_list = [star_graph, complete_graph]; //Assumes that q is larger than .5

var machine_list = [];
for (var i=0; i<ps.length; i++) {
	machine_list.push(new slot_machines.BernoulliMachine(ps[i]));
}

var machine_list_flipped = [];
for (var i=ps.length-1; i>=0; i--) {
	machine_list_flipped.push(new slot_machines.BernoulliMachine(ps[i]));
}

var agent_list = [];
for (var i=0; i<num_agents; i++) {
	switch (priors) {
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


var start_time = new Date().getTime();
var lock_times = {};

// Baseline, complete graph, no restrictions
lock_times["comp_succ"] = [];
lock_times["comp_inc"] = [];

var graph_list = [complete_graph, complete_graph];

for (var r=0; r<runs; r++) {
	var target = (ps[0] > ps[1]) ? 0 : 1;
	var network = new social_networks.DisseminationDummyNetwork(agent_list, machine_list, graph_list);

	if (randomize) {
	// Flip coin to determine order of machines and thus which machine is censored
		if (Math.random() < .5) {
			network = new social_networks.DisseminationDummyNetwork(agent_list, machine_list_flipped, graph_list);
			target = (target==1) ? 0 : 1;
		}
	}

	agent_list.forEach(function (a) {
		a.reset();
	});

	var dummy_choices = [];
	for (var t=0; t<steps; t++) {
		network.step();
		dummy_choices.unshift(network.getDummyChoice());
	}

	var last_choice = dummy_choices.shift();
	// var time_to_lock = dummy_choices.findIndex((x) => {return x!=last_choice} );
	var flipped = (last_choice==0) ? 1 : 0;
	var time_to_lock = dummy_choices.indexOf(flipped);

	if (time_to_lock == -1)
		time_to_lock = 1;
	else
		time_to_lock = steps - time_to_lock + 1; //The last choice was removed with the shift, plus the first step is step 0

	if (last_choice==target)
		lock_times["comp_succ"].push(time_to_lock);
	else
		lock_times["comp_inc"].push(time_to_lock);
}

// Restricting Dissemination
lock_times["diss_succ"] = [];
lock_times["diss_inc"] = [];

for (var r=0; r<runs; r++) {
	var target = (ps[0] > ps[1]) ? 0 : 1;
	var network = new social_networks.DisseminationDummyNetwork(agent_list, machine_list, graph_list);

	if (randomize) {
	// Flip coin to determine order of machines and thus which machine is censored
		if (Math.random() < .5) {
			network = new social_networks.DisseminationDummyNetwork(agent_list, machine_list_flipped, graph_list);
			target = (target==1) ? 0 : 1;
		}
	}

	agent_list.forEach(function (a) {
		a.reset();
	});

	var dummy_choices = [];
	for (var t=0; t<steps; t++) {
		network.step();
		dummy_choices.unshift(network.getDummyChoice());
	}

	var last_choice = dummy_choices.shift();
	// var time_to_lock = dummy_choices.findIndex((x) => {return x!=last_choice} );
	var flipped = (last_choice==0) ? 1 : 0;
	var time_to_lock = dummy_choices.indexOf(flipped);

	if (time_to_lock == -1)
		time_to_lock = 1;
	else
		time_to_lock = steps - time_to_lock + 1; //The last choice was removed with the shift, plus the first step is step 0

	if (last_choice==target)
		lock_times["diss_succ"].push(time_to_lock);
	else
		lock_times["diss_inc"].push(time_to_lock);
}

// Restricting Dissemination
lock_times["cond_succ"] = [];
lock_times["cond_inc"] = [];

for (var r=0; r<runs; r++) {
	var target = (ps[0] > ps[1]) ? 0 : 1;
	var network = new social_networks.ConductDummyNetwork(agent_list, machine_list, complete_graph, 1);

	if (randomize) {
	// Flip coin to determine order of machines and thus which machine is censored
		if (Math.random() < .5) {
			network = new social_networks.ConductDummyNetwork(agent_list, machine_list_flipped, complete_graph, 1);
			target = (target==1) ? 0 : 1;
		}
	}

	agent_list.forEach(function (a) {
		a.reset();
	});

	var dummy_choices = [];
	for (var t=0; t<steps; t++) {
		network.step();
		dummy_choices.unshift(network.getDummyChoice());
	}

	var last_choice = dummy_choices.shift();
	// var time_to_lock = dummy_choices.findIndex((x) => {return x!=last_choice} );
	var flipped = (last_choice==0) ? 1 : 0;
	var time_to_lock = dummy_choices.indexOf(flipped);

	if (time_to_lock == -1)
		time_to_lock = 1;
	else
		time_to_lock = steps - time_to_lock + 1; //The last choice was removed with the shift, plus the first step is step 0

	if (last_choice==target)
		lock_times["cond_succ"].push(time_to_lock);
	else
		lock_times["cond_inc"].push(time_to_lock);
}

// Restricting Both
lock_times["hybrid_succ"] = [];
lock_times["hybrid_inc"] = [];

for (var r=0; r<runs; r++) {
	var target = (ps[0] > ps[1]) ? 0 : 1;
	var network = new social_networks.HybridDummyNetwork(agent_list, machine_list, graph_list, 1);

	if (randomize) {
	// Flip coin to determine order of machines and thus which machine is censored
		if (Math.random() < .5) {
			network = new social_networks.HybridDummyNetwork(agent_list, machine_list_flipped, graph_list, 1);
			target = (target==1) ? 0 : 1;
		}
	}

	agent_list.forEach(function (a) {
		a.reset();
	});

	var dummy_choices = [];
	for (var t=0; t<steps; t++) {
		network.step();
		dummy_choices.unshift(network.getDummyChoice());
	}

	var last_choice = dummy_choices.shift();
	// var time_to_lock = dummy_choices.findIndex((x) => {return x!=last_choice} );
	var flipped = (last_choice==0) ? 1 : 0;
	var time_to_lock = dummy_choices.indexOf(flipped);

	if (time_to_lock == -1)
		time_to_lock = 1;
	else
		time_to_lock = steps - time_to_lock + 1; //The last choice was removed with the shift, plus the first step is step 0

	if (last_choice==target)
		lock_times["hybrid_succ"].push(time_to_lock);
	else
		lock_times["hybrid_inc"].push(time_to_lock);
}


// Print the results in a way that is easily readable by pandas
var lengths = [];
for (key in lock_times) {
	lengths.push(lock_times[key].length);
}

var m = Math.max.apply(null, lengths);

console.log("index,comp_succ,comp_inc,diss_succ,diss_inc,cond_succ,cond_inc,hybrid_succ,hybrid_inc");

for (var i=0; i<m; i++) {
	var s = i + ",";

	if (i<lock_times["comp_succ"].length)
		s+= lock_times["comp_succ"][i];
	s += ",";

	if (i<lock_times["comp_inc"].length)
		s+= lock_times["comp_inc"][i];
	s += ",";
	
	if (i<lock_times["diss_succ"].length)
		s+= lock_times["diss_succ"][i];
	s += ",";

	if (i<lock_times["diss_inc"].length)
		s+= lock_times["diss_inc"][i];
	s += ",";

	if (i<lock_times["cond_succ"].length)
		s+= lock_times["cond_succ"][i];
	s += ",";

	if (i<lock_times["cond_inc"].length)
		s+= lock_times["cond_inc"][i];
	s += ",";

	if (i<lock_times["hybrid_succ"].length)
		s+= lock_times["hybrid_succ"][i];
	s += ",";

	if (i<lock_times["hybrid_inc"].length)
		s+= lock_times["hybrid_inc"][i];
	
	console.log(s);
}

var end_time = new Date().getTime();
console.log("# " + (end_time-start_time)/1000/60 + " minutes elapsed");
