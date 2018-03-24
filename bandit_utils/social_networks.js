function Network(agents, machines, adjacencyMatrix) {
	this.agents = agents;
	this.machines = machines;
	this.adjacencyMatrix = adjacencyMatrix;

	this.getActs = function() {
		var acts = [];
		for (var i=0; i<this.agents.length; i++) {
				acts[i] = this.agents[i].getMachineToPlay();
		}
		return acts;
	}

	this.getPayouts = function(acts) {
		var payouts = [];
		for (var i=0; i<acts.length; i++) {
			payouts[i] = machines[acts[i]].pull();
		}
		return payouts;
	}

	this.step = function() {
		var acts = this.getActs();
		var payouts = this.getPayouts(acts);

		for (var i=0; i<this.adjacencyMatrix.length; i++) {
			for (var j=0; j<this.adjacencyMatrix.length; j++) {
				if (this.adjacencyMatrix[i][j] == 1)
					this.agents[i].update(acts[j],payouts[j]);
			}
		}
	}

	this.hasConvergedTo = function(target_index) {
		for (var i=0; i<this.agents.length; i++) {
			if (this.agents[i].getBestMachine() != target_index) {
				return false;
			}
		}
		return true;
	}

	this.hasReachedConsensus = function() {
		var m = this.agents[0].getMachineToPlay();
		return this.agents.every(function(a) {
			return a.getMachineToPlay() == m;
		});
		// Malfunctioned when get best machine returned a list
		// var m = this.agents[0].getBestMachine();
		// return this.agents.every(function(a) {
		// 	return a.getBestMachine() == m
		// });
	}
}

function DummyNetwork(agents, machines, adjacencyMatrix) {
	Network.call(this, agents, machines, adjacencyMatrix);

	this.hasDummyLearned = function(target_index) {
		// return this.agents[0].getBestMachine().some(x => x==target_index);
		return this.agents[0].getBestMachine().some( function(x) {
			return x==target_index;
		});
	}

	this.step = function() {
		var acts = this.getActs();
		var payouts = this.getPayouts(acts);
	
		for (var i=0; i<this.adjacencyMatrix.length; i++) {
			// The Dummy agents (index=0) does not actually act
			for (var j=1; j<this.adjacencyMatrix.length; j++) {
				if (this.adjacencyMatrix[i][j] == 1)
					this.agents[i].update(acts[j],payouts[j]);
			}
		}
	}

	this.getDummyChoice = function() {
		// return this.agents[0].getBestMachine()[0];
		// var x = this.agents[0].getMachineToPlay();
		return this.agents[0].getMachineToPlay();
	}
}

DummyNetwork.prototype = Object.create(Network.prototype);
DummyNetwork.prototype.constructor = DummyNetwork;

function DisseminationDummyNetwork(agents, machines, adjacency_matrices) {
	DummyNetwork.call(this, agents, machines, adjacency_matrices[0]);
	this.adjMatrices = adjacency_matrices;

	this.step = function() {
		var acts = this.getActs();
		var payouts = this.getPayouts(acts);

		for (var i=0; i<acts.length; i++) {
			// The dummy agent (index=0) does not actually act
			for (var j=1; j<acts.length; j++) {
				if (this.adjMatrices[acts[j]][i][j]==1)
					this.agents[i].update(acts[j], payouts[j]);
			}
		}
	}
}

DisseminationDummyNetwork.prototype = Object.create(DummyNetwork.prototype);
DisseminationDummyNetwork.prototype.constructor = DisseminationDummyNetwork;

// Will break if num_restricted is inconsistent with network size
function ConductDummyNetwork(agents, machines, adjacency_matrix, num_restricted) {
	DummyNetwork.call(this, agents, machines, adjacency_matrix);
	this.num_restricted = num_restricted;

	this.step = function() {
		var acts = this.getActs();

		// Agents indexed 1 through num_restricted are all forced to use act 0
		for (var i=1; i<=num_restricted; i++) {
			acts[i] = 0;
		}

		var payouts = this.getPayouts(acts);
	
		for (var i=0; i<acts.length; i++) {
			// The dummy agent (index=0) does not actually act
			for (var j=1; j<acts.length; j++) {
				if (this.adjacencyMatrix[i][j] == 1)
					this.agents[i].update(acts[j],payouts[j]);
			}
		}
	}
}

// Case recommended by a referee.  
// One agents is locked to arm 0, one agent is locked to arm 1, and the other agents are all free to choose
function SpecialConductDummyNetwork(agents, machines, adjacency_matrix) {
	DummyNetwork.call(this, agents, machines, adjacency_matrix);
	
	this.step = function() {
		var acts = this.getActs();

		//The agent indexed 1 is forced to use act 0
		//The agent indexed 2 is forced to use act 1
		acts[1] = 0;
		acts[2] = 1;

		var payouts = this.getPayouts(acts);

		for (var i=0; i<acts.length; i++) {
			for (var j=1; j<acts.length; j++) {
				if (this.adjacencyMatrix[i][j] == 1)
					this.agents[i].update(acts[j], payouts[j]);
			}
		}
	}
}

ConductDummyNetwork.prototype = Object.create(DummyNetwork.prototype);
ConductDummyNetwork.prototype.constructor = ConductDummyNetwork;


// Will break if num_restricted is inconsistent with network size
function HybridDummyNetwork(agents, machines, adjacency_matrices, num_restricted) {
	DummyNetwork.call(this, agents, machines, adjacency_matrices[0]);
	this.num_restricted = num_restricted;
	this.adjMatrices = adjacency_matrices;

	this.step = function() {
		var acts = this.getActs();

		// Agents indexed 1 through num_restricted are all forced to use act 0
		for (var i=1; i<=num_restricted; i++) {
			acts[i] = 0;
		}

		var payouts = this.getPayouts(acts);
	
		for (var i=0; i<acts.length; i++) {
			// The dummy agent (index=0) does not actually act
			for (var j=1; j<acts.length; j++) {
				if (this.adjMatrices[acts[j]][i][j]==1) 
					this.agents[i].update(acts[j], payouts[j]);
			}
		}
	}
}

HybridDummyNetwork.prototype = Object.create(DummyNetwork.prototype);
HybridDummyNetwork.prototype.constructor = HybridDummyNetwork;

//In all of these graphs the everyone sees the hub agent and the hub agent also pulls levers
function makeTwoCliquesGraph(numAgents) {
	var m = [];

	for(var i=0; i<numAgents; i++) {
		m[i] = [];
		for(var j=0; j<numAgents; j++) {
			if( (i<numAgents/2 && j<numAgents/2) || (i>=numAgents/2 && j>=numAgents/2) )
				m[i][j] = 1;
			else
				m[i][j] = 0;
		}
	}

	m[0][numAgents-1] = 1;
	m[numAgents-1][0] = 1;

	return m;
}

function makeStarGraph(numAgents) {
	var m = [];
	for (var i=0; i<numAgents; i++) {
		m[i] = [];
		for (var j=0; j<numAgents; j++) {
			if (i==0 || j==0 || i==j)
				m[i][j] = 1;
			else
				m[i][j] = 0;
		}
	}
	return m;
}

function makeCompleteGraph(numAgents) {
	var m = [];
	for (var i=0; i<numAgents; i++) {
		m[i] = [];
		for (var j=0; j<numAgents; j++) {
			m[i][j] = 1;
		}
	}
	return m;
}

function makeKCycleGraph(numAgents, k) {
	var m = [];
	for (var i=0; i<numAgents; i++) {
		m[i] = [];
		for (var j=0; j<numAgents; j++) {
			m[i][j] = 0;
		}
	}

	for (var i=0; i<numAgents; i++) {
		for (var j=0; j<=k; j++) {
			var u = (i+j)%numAgents;
			var l = (i>=j) ? i-j : numAgents+i-j;

			m[i][u] = 1;
			m[i][l] = 1;
		}
	}

	return m;
}

function makeCycleGraph(numAgents) {
	return makeKCycleGraph(numAgents, 1);
}

function makeWheelGraph(numAgents) {
	var g = makeCycleGraph(numAgents);

	for (var j=1; j<numAgents; j++) {
		g[0][j] = 1;
		g[j][0] = 1;
	}

	return g;
}

function makeLineGraph(numAgents) {
	var m = [];
	for (var i=0; i<numAgents; i++) {
		m[i] = [];
		for(var j=0; j<numAgents; j++) {
			if (i==j)
				m[i][j] = 1;
			else if (j==(i+1) || j==(i-1))
				m[i][j] = 1;
			else
				m[i][j] = 0;
		}
	}
	return m;
}

module.exports.Network = Network;
module.exports.DummyNetwork = DummyNetwork;
module.exports.DisseminationDummyNetwork = DisseminationDummyNetwork;
module.exports.ConductDummyNetwork = ConductDummyNetwork;
module.exports.SpecialConductDummyNetwork = SpecialConductDummyNetwork;
module.exports.HybridDummyNetwork = HybridDummyNetwork;

module.exports.makeTwoCliquesGraph = makeTwoCliquesGraph;
module.exports.makeStarGraph = makeStarGraph;
module.exports.makeLineGraph = makeLineGraph;
module.exports.makeCycleGraph = makeCycleGraph;
module.exports.makeWheelGraph = makeWheelGraph;
module.exports.makeCompleteGraph = makeCompleteGraph;
module.exports.makeKCycleGraph = makeKCycleGraph;