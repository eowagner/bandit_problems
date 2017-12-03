# node_bandits

To generate data and figures used in the paper "Agent-based models of dual-use research", run

./simulate_durc_paper.sh

It requires:

	* nodejs (with minimist from npm) for data generation

And

	* python 3 (with pandas and seaborn) for figure construction

Output, incuding figures, will be located in the directory out/timestamp, where timestamp is an id indicating the time in which the bash file was executed.