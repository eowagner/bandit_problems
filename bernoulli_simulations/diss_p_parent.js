var child_process = require('child_process');
var argv = require('minimist')(process.argv.slice(2));

var slot_machines = require('../bandit_utils/slot_machines.js');
var beta_agents = require('../bandit_utils/agents.js');
var social_networks = require('../bandit_utils/social_networks.js');

const numCPUs = require('os').cpus().length;
// const numCPUs = 1;
console.log("# Number of cores: " + numCPUs);

var runs = 10;
var steps = 1000;
var num_agents = 9;
var priors = "uniform";
var which_arm_restricted = "randomize"; //low, or high

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

var p_list = [];
for (var q=.505; q<=.805; q+=.005) {
	p_list.push(q);
}

console.log("# Priors: " + priors + "; runs: " + runs + "; steps: " + steps);
console.log("# Which arm is restricted: " + which_arm_restricted);
console.log("num_agents,p0,p1,success,consensus");

var results_as_strings = [];

//Global required for traversing the independent variable over multiple child processes
//And then determining that every independent variable has completed 
var proc_index = 0; 
var completed_processes = 0;

var start_time = new Date().getTime();

for (var i=0; i<numCPUs; i++) {
	launch_next_child();
}

function launch_next_child() {
	if (proc_index >= p_list.length)
		return;	

	var complete_graph = social_networks.makeCompleteGraph(num_agents);
	var star_graph = social_networks.makeStarGraph(num_agents);

	var graph_list = [complete_graph, star_graph];
	var randomize = (which_arm_restricted=="randomize") ? true : false;
	if (which_arm_restricted=="low")
		graph_list = [star_graph, complete_graph];

	var parameters = {
		priors: priors,
		p: [.5, p_list[proc_index]],
		runs: runs,
		steps: steps,
		randomize: randomize,
		graphs: graph_list
		// graphs: [star_graph, complete_graph]
		// graphs: [star_graph, star_graph]
		// graphs: [complete_graph, complete_graph]
	};

	proc_index++;

	var child = child_process.fork('./bernoulli_simulations/diss_child.js');

	child.send(parameters);

	child.on('message', function(message) {
		console.log(convert_results_to_string(message));

		launch_next_child();

		completed_processes++;
		if (completed_processes >= p_list.length) {
			var end_time = new Date().getTime();
			console.log("# " + (end_time-start_time)/1000/60 + " minutes elapsed");
		}
		
	});
}


function convert_results_to_string(res) {
	var s = res.parameters.graphs[0].length + "," + res.parameters.p[0] + "," + res.parameters.p[1] + ",";

	s += res.success_count + ",";
	s += res.consensus_count;

	return s;
}