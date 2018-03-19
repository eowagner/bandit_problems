#!/bin/bash

TIMESTAMP="$(date +%Y%m%d%H%M%S)"
DNAME="out/$TIMESTAMP"
# RUNS=100000
RUNS=10000
PROG="nodejs"

mkdir -p $DNAME

$PROG bernoulli_simulations/baseline_agents_parent.js -p uniform -r $RUNS -s 1000 -q .6 | tee "$DNAME/baseline-agents-6.csv"
$PROG bernoulli_simulations/special_conduct_parent.js -p uniform -r $RUNS -s 1000 -n 1 -c randomize -q .6 | tee "$DNAME/special-conduct-agents-6.csv"
$PROG bernoulli_simulations/conduct_agents_parent.js -p uniform -r $RUNS -s 1000 -n 2 -c randomize -q .6 | tee "$DNAME/conduct-agents-6.csv"
$PROG bernoulli_simulations/baseline_p_parent.js -p uniform -r $RUNS -s 1000 -n 9 | tee "$DNAME/baseline-p.csv"
$PROG bernoulli_simulations/diss_p_parent.js -p uniform -r $RUNS -s 1000 -n 9 -c randomize | tee "$DNAME/star-p.csv"
$PROG bernoulli_simulations/alt_structs_diss_p_parent.js -p uniform -r $RUNS -s 1000 -n 9 -c randomize -a cycle | tee "$DNAME/cycle-p.csv"
$PROG bernoulli_simulations/alt_structs_diss_p_parent.js -p uniform -r $RUNS -s 1000 -n 9 -c randomize -a wheel | tee "$DNAME/wheel-p.csv"