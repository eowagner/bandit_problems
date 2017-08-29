//Compares Dummy Complete to Dummy Star, with no restrictions on either dissemination or conduct

var slot_machines = require('./bandit_utils/slot_machines.js');
var beta_agents = require('./bandit_utils/beta_agents.js');
var social_networks = require('./bandit_utils/social_networks.js');
var fs = require('fs');

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
var cycleGraph = social_networks.makeCycleGraph(agent_list.length);


// var dummyComplete = new social_networks.DummyNetwork(agent_list, machine_list, completeGraph);
var netComplete = new social_networks.DummyNetwork(agent_list, machine_list, completeGraph);
var netCycle = new social_networks.DummyNetwork(agent_list, machine_list, cycleGraph);


var start_time = new Date().getTime();

var p_list = [];
var succ_complete = [];
var succ_cycle = [];
var index = 0;

for (var p=.505; p<=.7; p+=.005) {
	p_list.push(p);
	succ_complete.push(0);
	succ_cycle.push(0);

	machine_list = [new slot_machines.BernoulliMachine(.5), new slot_machines.BernoulliMachine(p)];
	netComplete = new social_networks.DummyNetwork(agent_list, machine_list, completeGraph);
	netCycle = new social_networks.DummyNetwork(agent_list, machine_list, cycleGraph);

	for (var r=0; r<runs; r++) {
		agent_list.forEach(function(a) {
			// a.resetUniformPriors();
			a.resetRandomInterval([0,4], [0,4]);
		});

		for (var t=0; t<steps; t++) {
			netComplete.step();
		}

		if (netComplete.hasDummyLearned(1))
			succ_complete[index]++;
	}

	for (var r=0; r<runs; r++) {
		agent_list.forEach(function(a) {
			a.resetUniformPriors();
		});

		for (var t=0; t<steps; t++) {
			netCycle.step();
		}

		if (netCycle.hasDummyLearned(1))
			succ_cycle[index]++;
	}

	console.log(p + ": " + succ_complete[index] + ", " + succ_cycle[index]);
	index++;
}

var end_time = new Date().getTime();


console.log("Minutes elapsed: " + (end_time - start_time)/1000/60);


var info = "num_agents: " + num_agents + "; runs: " + runs + "; steps: " + steps;
var stream = fs.createWriteStream(end_time + ".csv");
stream.once('open', function(fd) {
	stream.write("# " + info + "\n");

	stream.write('p,succ_compltee,succ_cycle\n');

	for(var i=0; i<p_list.length; i++) {
		stream.write(p_list[i]+","+succ_complete[i]+","+succ_cycle[i]+"\n");
	}

	stream.end();
});
