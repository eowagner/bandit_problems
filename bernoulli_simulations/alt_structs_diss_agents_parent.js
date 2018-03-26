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
var alt_graph_name = "cycle";
var k = 1;

if ('p' in argv)
	priors = argv['p'];

if ('r' in argv)
	runs = argv['r'];

if ('s' in argv)
	steps = argv['s'];

if ('q' in argv)
	q = argv['q']

if ('c' in argv)
	which_arm_restricted = argv['c'];

if ('a' in argv)
	alt_graph_name = argv['a'];

	if (alt_graph_name == 'kcycle' && 'k' in argv)
		var k = argv['k'];

var num_agent_list = [];
var smallest = 4;
for (var i=smallest; i<41; i++) {
	num_agent_list.push(i);
}

console.log("# Priors: " + priors + "; runs: " + runs + "; steps: " + steps);
console.log("# Which arm is restricted: " + which_arm_restricted);
console.log("# Graph structure: " + alt_graph_name);
console.log("num_agents,p0,p1,success,consensus,time,success_time,incorrect_time");

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

	var alt_graph;
	switch (alt_graph_name) {
		case "wheel":
			alt_graph = social_networks.makeWheelGraph(num_agent_list[proc_index]);
			break;
		case "twocliques":
			alt_graph = social_networks.makeTwoCliquesGraph(num_agent_list[proc_index]);
			break;
		case "kcycle":
			alt_graph = social_networks.makeKCycleGraph(num_agent_list[proc_index], k);
			break;
		default:
			alt_graph = social_networks.makeCycleGraph(num_agent_list[proc_index]);
	}

	var ps = [.5, q];

	var graph_list = [complete_graph, alt_graph];

	var randomize = (which_arm_restricted=="randomize") ? true : false;
	if (which_arm_restricted=="low")
		graph_list = [alt_graph, complete_graph];

	var parameters = {
		priors: priors,
		p: ps,
		runs: runs,
		steps: steps,
		randomize: randomize,
		graphs: graph_list
	};

	proc_index++;

	var child = child_process.fork('./bernoulli_simulations/diss_child.js');

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
	var s = res.parameters.graphs[0].length + "," + res.parameters.p[0] + "," + res.parameters.p[1] + ",";

	s += res.success_count + ",";
	s += res.consensus_count + ",";
	s += res.total_time_to_lock + "," + res.total_time_to_successful_lock + "," + res.total_time_to_incorrect_lock;

	return s;
}