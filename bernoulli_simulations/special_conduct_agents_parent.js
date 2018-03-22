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
var priors = "uniform";
var which_arm_restricted = "randomize"; //low, or high
var num_restricted = 2;
var q = .6;


if ('p' in argv)
	priors = argv['p'];

if ('r' in argv)
	runs = argv['r'];

if ('s' in argv)
	steps = argv['s'];

if ('c' in argv)
	which_arm_restricted = argv['c'];

if ('q' in argv)
	q = argv['q']


console.log("# Priors: " + priors + "; runs: " + runs + "; steps: " + steps);

console.log("# Number of agents who are limited to just one arm: " + num_restricted);

console.log("num_agents,p0,p1,success");

var num_agent_list = [];
var smallest = 4;
for (var i=smallest; i<41; i++) {
	num_agent_list.push(i);
}

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
	if (proc_index >= num_agent_list.length)
		return;	

	var complete_graph = social_networks.makeCompleteGraph(num_agent_list[proc_index]);

	var ps = [.5, q];
	var randomize = (which_arm_restricted=="randomize") ? true : false;
	if (which_arm_restricted=="low")
		ps = [q, .5];

	var parameters = {
		priors: priors,
		p: ps,
		runs: runs,
		steps: steps,
		graph: complete_graph,
		randomize: randomize
	};

	proc_index++;

	var child = child_process.fork('./bernoulli_simulations/special_conduct_child.js');

	child.send(parameters);

	child.on('message', function(message) {
		console.log(convert_results_to_string(message));

		launch_next_child();

		completed_processes++;
		if (completed_processes >= num_agent_list.length) {
			var end_time = new Date().getTime();
			console.log("# " + (end_time-start_time)/1000/60 + " minutes elapsed");
		}
		
	});
}


function convert_results_to_string(res) {
	var s = res.parameters.graph.length + "," + res.parameters.p[0] + "," + res.parameters.p[1] + "," + res.success_counts;

	return s;
}