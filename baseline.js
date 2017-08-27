//Compares Dummy Complete to Dummy Star, with no restrictions on either dissemination or conduct

var slot_machines = require('./bandit_utils/slot_machines.js');
var beta_agents = require('./bandit_utils/beta_agents.js');
var social_networks = require('./bandit_utils/social_networks.js');

var num_agents = 9;
var runs = 1000;
var steps = 1000;

var agent_list = new Array(num_agents);
for (var i=0; i<num_agents; i++) {
	agent_list[i] = new beta_agents.BetaAgent(2);
}

var p = .505;


var machine_list = [new slot_machines.BernoulliMachine(.5), new slot_machines.BernoulliMachine(p)];

var completeGraph = social_networks.makeCompleteGraph(agent_list.length);
var cycleGraph = social_networks.makeCompleteGraph(agent_list.length);


var dummyComplete = new social_networks.DummyNetwork(agent_list, machine_list, completeGraph);


var start_time = new Date().getTime();

var p_list = [];
var succ_counts = [];
var index = 0;

for (var p=.51; p<.7; p+=.005) {
	p_list.push(p);
	succ_counts.push(0);

	machine_list = [new slot_machines.BernoulliMachine(.5), new slot_machines.BernoulliMachine(p)];
	dummyComplete = new social_networks.DummyNetwork(agent_list, machine_list, completeGraph);

	for (var r=0; r<runs; r++) {
		agent_list.forEach(function(a) {
			a.resetUniformPriors();
		});

		for (var t=0; t<steps; t++) {
			dummyComplete.step();
		}

		if (dummyComplete.hasDummyLearned(1))
			succ_counts[index]++;
	}

	console.log(p);
	console.log(succ_counts[index]);
	index++;
}

var end_time = new Date().getTime();

console.log(succ_counts);

console.log((end_time - start_time)/1000/60);