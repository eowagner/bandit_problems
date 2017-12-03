#!/bin/bash

TIMESTAMP="$(date +%Y%m%d%H%M%S)"
DNAME="out/$TIMESTAMP"
RUNS=100000
# RUNS=2
PROG="nodejs"

mkdir -p $DNAME

$PROG bernoulli_simulations/time.js -r $RUNS -s 1000 -q .6 | tee "$DNAME/time-6.csv"
$PROG bernoulli_simulations/time.js -r $RUNS -s 1000 -q .8 | tee "$DNAME/time-8.csv"
$PROG bernoulli_simulations/baseline_p_parent.js -p uniform -r $RUNS -s 1000 -n 9 | tee "$DNAME/baseline-p.csv"
$PROG bernoulli_simulations/baseline_agents_parent.js -p uniform -r $RUNS -s 1000 -q .6 | tee "$DNAME/baseline-agents-6.csv"
$PROG bernoulli_simulations/diss_p_parent.js -p uniform -r $RUNS -s 1000 -n 9 -c randomize| tee "$DNAME/diss-p-randomized.csv"
$PROG bernoulli_simulations/diss_agents_parent.js -p uniform -r $RUNS -s 1000 -q .6 -c randomize | tee "$DNAME/diss-agents-6-randomized.csv"
$PROG bernoulli_simulations/conduct_p_parent.js -p uniform -r $RUNS -s 1000 -n 9 -c randomize | tee "$DNAME/conduct-randomized.csv"
$PROG bernoulli_simulations/conduct_agents_parent.js -p uniform -r $RUNS -s 1000 -n 1 -c randomize | tee "$DNAME/conduct-agents-1.csv"
$PROG bernoulli_simulations/conduct_agents_parent.js -p uniform -r $RUNS -s 1000 -n 2 -c randomize | tee "$DNAME/conduct-agents-2.csv"
$PROG bernoulli_simulations/conduct_agents_parent.js -p uniform -r $RUNS -s 1000 -n 3 -c randomize | tee "$DNAME/conduct-agents-3.csv"
$PROG bernoulli_simulations/hybrid_p_parent.js -p uniform -r $RUNS -s 1000 -n 9 -c randomize | tee "$DNAME/hybrid-randomized.csv"
python scatterplots.py "$DNAME/"
python time_histograms.py "$DNAME/"