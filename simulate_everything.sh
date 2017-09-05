#!/bin/bash

RUNS=1000
echo "Baseline p"
nodejs baseline_p_parent.js -p uniform -r $RUNS -s 1000 -n 9
echo "Baseline agents, q=.55"
nodejs baseline_agents_parent.js -p uniform -r $RUNS -s 1000 -q .55
echo "Baseline agents, q=.6"
nodejs baseline_agents_parent.js -p uniform -r $RUNS -s 1000 -q .6
echo "Dissemination p"
nodejs dissemination_p_parent.js -p uniform -r $RUNS -s 1000 -n 9
echo "Dissemination agents, q=.55"
nodejs dissemination_agents_parent.js -p uniform -r $RUNS -s 1000 -q .55 
echo "Dissemination agents, q=.55"
nodejs dissemination_agents_parent.js -p uniform -r $RUNS -s 1000 -q .6 
echo "Conduct p"
nodejs conduct_p_parent.js -p uniform -r $RUNS -s 1000 -n 9
