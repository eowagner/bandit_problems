import pandas
import matplotlib.pyplot as plt
from matplotlib import cm
from numpy import linspace
import seaborn as sns
import sys

if len(sys.argv) < 2:
	dirname = 'out/test/'
else:
	dirname = sys.argv[1]

start = 0.0
stop = 1.0
number_of_colors= 8
cm_subsection = linspace(start, stop, number_of_colors) 
circular_colors = [ cm.jet(x) for x in cm_subsection ]

markers = ["o", "+", "x", "^", "p"]

colors = [sns.xkcd_rgb["pale red"]]

xkcdnames = ["windows blue", "amber", "greyish", "faded green", "dusty purple"]
xkcdnames = ["windows blue", "dusty purple", "faded green", "amber", "greyish"]
colors = [sns.xkcd_rgb[n] for n in xkcdnames]

plt.style.use('seaborn')

baseline = pandas.read_csv(dirname + 'baseline-p.csv', comment="#")
baseline_agents = pandas.read_csv(dirname + 'baseline-agents-6.csv', comment="#")

diss_p_rand = pandas.read_csv(dirname + 'diss-p-randomized.csv', comment="#")

diss_agents_rand = pandas.read_csv(dirname + 'diss-agents-6-randomized.csv', comment="#")

conduct_rand = pandas.read_csv(dirname + 'conduct-randomized.csv', comment="#")

conduct_agents_1 = pandas.read_csv(dirname + 'conduct-agents-1.csv', comment="#")
conduct_agents_2 = pandas.read_csv(dirname + 'conduct-agents-2.csv', comment="#")
conduct_agents_3 = pandas.read_csv(dirname + 'conduct-agents-3.csv', comment="#")

hybrid_rand = pandas.read_csv(dirname + 'hybrid-randomized.csv', comment="#")

ax_diss = diss_p_rand.plot(kind="scatter", x="p1", y="success", color=colors[0], marker=markers[0], label="Dissemination is restricted")
baseline.plot(kind="scatter", x="p1", y="success_complete", color=colors[3], marker=markers[3], label="No restrictions", ax=ax_diss)
ax_diss.set_xlabel("p")
ax_diss.set_ylabel("Number of trials that resulted in successful learning")
ax_diss.set_title("Restricting Dissemination")
plt.savefig(dirname + "Fig1.pdf")

ax_diss_agents = diss_agents_rand.plot(kind="scatter", x="num_agents", y="success", color=colors[0], marker=markers[0], label="Dissemination is restricted")
baseline_agents.plot(kind="scatter", x="num_agents", y="success_complete", color=colors[3], marker=markers[3], label="No restrictions", ax=ax_diss_agents)
ax_diss_agents.set_xlabel("Number of agents")
ax_diss_agents.set_ylabel("Number of trials that resulted in successful learning")
ax_diss_agents.set_title("Restricting Dissemination, p = .6")
plt.savefig(dirname + "Fig2.pdf")

ax_conduct_agents = conduct_agents_1.plot(kind="scatter", x="num_agents", y="success", color=colors[0], marker=markers[0], label="1 agent limited")
conduct_agents_2.plot(kind="scatter", x="num_agents", y="success", color=colors[1], marker=markers[1], label="2 agents limited", ax=ax_conduct_agents)
conduct_agents_3.plot(kind="scatter", x="num_agents", y="success", color=colors[2], marker=markers[2], label="3 agents limited", ax=ax_conduct_agents)
baseline_agents.plot(kind="scatter", x="num_agents", y="success_complete", color=colors[3], marker=markers[3], label="No restrictions", ax=ax_conduct_agents)
ax_conduct_agents.set_xlabel("Number of agents")
ax_conduct_agents.set_ylabel("Number of trials that resulted in successful learning")
ax_conduct_agents.set_title("Restricting Conduct, p = .6")
plt.savefig(dirname + "Fig4.pdf")

ax_conduct_rand = conduct_rand.plot(kind="scatter", x="p1", y="1_res_success", color=circular_colors[0], label="7 dual-use agents")
conduct_rand.plot(kind="scatter", x="p1", y="2_res_success", color=circular_colors[1], label="6 dual-use agents", ax=ax_conduct_rand)
conduct_rand.plot(kind="scatter", x="p1", y="3_res_success", color=circular_colors[2], label="5 dual-use agents", ax=ax_conduct_rand)
conduct_rand.plot(kind="scatter", x="p1", y="4_res_success", color=circular_colors[3], label="4 dual-use agents", ax=ax_conduct_rand)
conduct_rand.plot(kind="scatter", x="p1", y="5_res_success", color=circular_colors[4], label="3 dual-use agents", ax=ax_conduct_rand)
conduct_rand.plot(kind="scatter", x="p1", y="6_res_success", color=circular_colors[5], label="2 dual-use agents", ax=ax_conduct_rand)
conduct_rand.plot(kind="scatter", x="p1", y="7_res_success", color=circular_colors[6], label="1 dual-use agent", ax=ax_conduct_rand)
baseline.plot(kind="scatter", x="p1", y="success_complete", color=circular_colors[7], marker=markers[3], label="No restrictions", ax=ax_conduct_rand)
ax_conduct_rand.set_xlabel("p")
ax_conduct_rand.set_ylabel("Number of trials that resulted in successful learning")
ax_conduct_rand.set_title("Restricting Conduct")
plt.savefig(dirname + "Fig3.pdf")

ax_hybrid_rand = hybrid_rand.plot(kind="scatter", x="p1", y="1_res_success", color=circular_colors[0], label="7 dual-use agents")
hybrid_rand.plot(kind="scatter", x="p1", y="2_res_success", color=circular_colors[1], label="6 dual-use agents", ax=ax_hybrid_rand)
hybrid_rand.plot(kind="scatter", x="p1", y="3_res_success", color=circular_colors[2], label="5 dual-use agents", ax=ax_hybrid_rand)
hybrid_rand.plot(kind="scatter", x="p1", y="4_res_success", color=circular_colors[3], label="4 dual-use agents", ax=ax_hybrid_rand)
hybrid_rand.plot(kind="scatter", x="p1", y="5_res_success", color=circular_colors[4], label="3 dual-use agents", ax=ax_hybrid_rand)
hybrid_rand.plot(kind="scatter", x="p1", y="6_res_success", color=circular_colors[5], label="2 dual-use agents", ax=ax_hybrid_rand)
hybrid_rand.plot(kind="scatter", x="p1", y="7_res_success", color=circular_colors[6], label="1 dual-use agent", ax=ax_hybrid_rand)
baseline.plot(kind="scatter", x="p1", y="success_complete", color=circular_colors[7], marker=markers[3], label="No restrictions", ax=ax_hybrid_rand)
ax_hybrid_rand.set_xlabel("p")
ax_hybrid_rand.set_ylabel("Number of trials that resulted in successful learning")
ax_hybrid_rand.set_title("Restricting both Dissemination and Conduct")
plt.savefig(dirname + "Fig5.pdf")

ax_reg_comp = hybrid_rand.plot(kind="scatter", x="p1", y="1_res_success", color=colors[0], marker=markers[0], label="Both conduct and dissemination are restricted")
diss_p_rand.plot(kind="scatter", x="p1", y="success", label="Only dissemination is restricted", color=colors[1], marker=markers[1], ax=ax_reg_comp)
conduct_rand.plot(kind="scatter", x="p1", y="1_res_success", label="Only conduct is restricted", color=colors[2], marker=markers[2], ax=ax_reg_comp)
baseline.plot(kind="scatter", x="p1", y="success_complete", label="No restrictions", color=colors[3], marker=markers[3], ax=ax_reg_comp)
ax_reg_comp.set_xlabel("p")
ax_reg_comp.set_ylabel("Number of trials that resulted in successful learning")
ax_reg_comp.set_title("Comparing Regulatory Schemes")
plt.savefig(dirname + "Fig6.pdf")