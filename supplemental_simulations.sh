#!/bin/bash

TIMESTAMP="$(date +%Y%m%d%H%M%S)"
DNAME="out/$TIMESTAMP"
# RUNS=100000
RUNS=1000
PROG="nodejs"

mkdir -p $DNAME

$PROG bernoulli_simulations/baseline_p_parent.js -p uniform -r $RUNS -s 1000 -n 9 | tee "$DNAME/baseline-p.csv"
$PROG bernoulli_simulations/conduct_p_parent.js -p uniform -r $RUNS -s 1000 -n 9 -c randomize | tee "$DNAME/conduct-randomized.csv"
$PROG bernoulli_simulations/special_conduct_p_parent.js -p uniform -r $RUNS -s 1000 -n 9 | tee "$DNAME/special-conduct-p.csv"
# $PROG bernoulli_simulations/special_conduct_agents_parent.js -p uniform -r $RUNS -s 1000 -q .6 | tee "$DNAME/special-conduct-agents-6.csv"
# $PROG bernoulli_simulations/alt_structs_diss_p_parent.js -p uniform -r $RUNS -s 1000 -n 9 -c randomize -a kcycle -k 1 | tee "$DNAME/cycle-1-p.csv"
# $PROG bernoulli_simulations/alt_structs_diss_p_parent.js -p uniform -r $RUNS -s 1000 -n 9 -c randomize -a kcycle -k 2 | tee "$DNAME/cycle-2-p.csv"
# $PROG bernoulli_simulations/alt_structs_diss_p_parent.js -p uniform -r $RUNS -s 1000 -n 9 -c randomize -a kcycle -k 3 | tee "$DNAME/cycle-3-p.csv"
# $PROG bernoulli_simulations/alt_structs_diss_p_parent.js -p uniform -r $RUNS -s 1000 -n 9 -c randomize -a wheel | tee "$DNAME/wheel-p.csv"

# $PROG bernoulli_simulations/alt_structs_diss_agents_parent.js -p uniform -r $RUNS -s 1000 -q .6 -a kcycle -k 1 | tee "$DNAME/cycle-1-agents.csv"
# $PROG bernoulli_simulations/alt_structs_diss_agents_parent.js -p uniform -r $RUNS -s 1000 -q .6 -a kcycle -k 2 | tee "$DNAME/cycle-2-agents.csv"
# $PROG bernoulli_simulations/alt_structs_diss_agents_parent.js -p uniform -r $RUNS -s 1000 -q .6 -a kcycle -k 3 | tee "$DNAME/cycle-3-agents.csv"
# $PROG bernoulli_simulations/alt_structs_diss_agents_parent.js -p uniform -r $RUNS -s 1000 -q .6 -a wheel | tee "$DNAME/wheel-agents.csv"