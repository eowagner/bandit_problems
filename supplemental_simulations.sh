#!/bin/bash

TIMESTAMP="$(date +%Y%m%d%H%M%S)"
DNAME="out/$TIMESTAMP"
# RUNS=100000
RUNS=1000
PROG="nodejs"

mkdir -p $DNAME

$PROG bernoulli_simulations/baseline_agents_parent.js -p uniform -r $RUNS -s 1000 -q .55 | tee "$DNAME/baseline-agents-6.csv"
$PROG bernoulli_simulations/double_conduct_agents_parent.js -p uniform -r $RUNS -s 1000 -n 1 -c randomize -q .55 | tee "$DNAME/special-conduct-agents.csv"
$PROG bernoulli_simulations/conduct_agents_parent.js -p uniform -r $RUNS -s 1000 -n 2 -c randomize -q .55 | tee "$DNAME/conduct-agents-2.csv"