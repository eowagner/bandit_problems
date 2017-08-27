var slot_machines = require('./bandit_utils/slot_machines.js');
var beta_agents = require('./bandit_utils/beta_agents.js');
var social_networks = require('./bandit_utils/social_networks.js');

var num_agents = 10;

var machine_list = [new slot_machines.BernoulliMachine(.5), new slot_machines.BernoulliMachine(.51)];

var agent_list = new Array(num_agents);
for (var i=0; i<num_agents; i++) {
	agent_list[i] = new beta_agents.BetaAgent(machine_list.length);
}


var completeGraph = social_networks.makeCompleteGraph(agent_list.length);
var cycleGraph = social_networks.makeCompleteGraph(agent_list.length);

var comp_cycle_net = new social_networks.DoubleDummyNetwork(agent_list, machine_list, completeGraph, cycleGraph);

var start_time = new Date().getTime();

var succ_count = 0;

for (var r=0; r<1000; r++) {
	agent_list.forEach(function(a) {
		a.reset();
	});

	for (var t=0; t<1000; t++) {
		comp_cycle_net.step();
	}

	if (comp_cycle_net.hasDummyLearned(1))
		succ_count++;
}

var end_time = new Date().getTime();

console.log(succ_count);

console.log((end_time - start_time)/1000/60);