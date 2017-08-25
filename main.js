var slot_machines = require('./bandit_utils/slot_machines.js');
var beta_agents = require('./bandit_utils/beta_agents.js');
var social_networks = require('./bandit_utils/social_networks.js');

var num_agents = 10;

var machine_list = [new slot_machines.BernoulliMachine(.5), new slot_machines.BernoulliMachine(.51)];

var agent_list = new Array(num_agents);
for (var i=0; i<num_agents; i++) {
	agent_list[i] = new beta_agents.BetaAgent(machine_list.length);
}


var net = new social_networks.Network(agent_list, machine_list, social_networks.makeCompleteGraph(agent_list.length));

for (var t=0; t<100; t++) {
	net.step();	
}

console.log(net.hasConvergedTo(1));