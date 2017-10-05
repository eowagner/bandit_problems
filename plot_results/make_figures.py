import pandas
import matplotlib.pyplot as plt
from matplotlib import cm
from numpy import linspace

dirname = 'bernoulli-100k/'

start = 0.0
stop = 1.0
number_of_colors= 8
cm_subsection = linspace(start, stop, number_of_colors) 
colors = [ cm.jet(x) for x in cm_subsection ]

markers = ["o", "+", "x", "^"]

baseline = pandas.read_csv(dirname + 'baseline-p.csv', comment="#")
baseline_agents = pandas.read_csv(dirname + 'baseline-agents-55.csv', comment="#")

diss_p_rand = pandas.read_csv(dirname + 'diss-p-randomized.csv', comment="#")
diss_p_low = pandas.read_csv(dirname + 'diss-p-low.csv', comment="#")
diss_p_high = pandas.read_csv(dirname + 'diss-p-high.csv', comment="#")

# # dissemination_agents = pandas.read_csv(dirname + 'diss-agents-55.csv', comment="#")
conduct = pandas.read_csv(dirname + 'conduct.csv', comment="#")
hybrid = pandas.read_csv(dirname + 'hybrid.csv', comment="#")


ax_baseline = baseline.plot(kind="scatter", x="p1", y="success_star", color=colors[0], marker=markers[0], label="Star graph")
baseline.plot(kind="scatter", x="p1", y="success_complete", label="Complete graph", color=colors[7], marker=markers[1], ax=ax_baseline)
ax_baseline.set_xlabel("p")
ax_baseline.set_ylabel("Number of trials that resulted in successful learning")
plt.savefig("baseline.pdf")

ax_baseline_agents = baseline_agents.plot(kind="scatter", x="num_agents", y="success_star", color=colors[0], label="Star graph")
baseline_agents.plot(kind="scatter", x="num_agents", y="success_complete", color=colors[7], label="Complete graph", marker="+", ax=ax_baseline_agents)
ax_baseline.set_xlabel("Number of agents")
ax_baseline.set_ylabel("Number of trials that resulted in successful learning")
plt.savefig("baseline-agents.pdf")

ax_diss = diss_p_rand.plot(kind="scatter", x="p1", y="success", color=colors[0], marker=markers[0], label="Random arm's dissemination restricted")
diss_p_low.plot(kind="scatter", x="p1", y="success", color=colors[3], marker=markers[2], label="Low arm's dissemination restricted", ax=ax_diss)
diss_p_high.plot(kind="scatter", x="p1", y="success", color=colors[5], marker=markers[3], label="High arm's dissemination restricted", ax=ax_diss)
baseline.plot(kind="scatter", x="p1", y="success_complete", color=colors[7], marker=markers[1], label="No restrictions", ax=ax_diss)
ax_diss.set_xlabel("p")
ax_diss.set_ylabel("Number of trials that resulted in successful learning")
plt.savefig("dissemination.pdf")


ax_conduct = conduct.plot(kind="scatter", x="p1", y="1_res_success", color=colors[0], label="1 restricted agent")
conduct.plot(kind="scatter", x="p1", y="2_res_success", color=colors[1], label="2 restricted agents", ax=ax_conduct)
conduct.plot(kind="scatter", x="p1", y="3_res_success", color=colors[2], label="3 restricted agents", ax=ax_conduct)
conduct.plot(kind="scatter", x="p1", y="4_res_success", color=colors[3], label="4 restricted agents", ax=ax_conduct)
conduct.plot(kind="scatter", x="p1", y="5_res_success", color=colors[4], label="5 restricted agents", ax=ax_conduct)
conduct.plot(kind="scatter", x="p1", y="6_res_success", color=colors[5], label="6 restricted agents", ax=ax_conduct)
conduct.plot(kind="scatter", x="p1", y="7_res_success", color=colors[6], label="7 restricted agents", ax=ax_conduct)
baseline.plot(kind="scatter", x="p1", y="success_complete", color=colors[7], label="No restrictions", ax=ax_conduct)
ax_conduct.set_xlabel("p")
ax_conduct.set_ylabel("Number of trials that resulted in successful learning")
plt.savefig("conduct.pdf")

ax_hybrid = hybrid.plot(kind="scatter", x="p1", y="1_res_success", color=colors[0], marker=markers[0], label="Hybrid, with 1 agent limited")
diss_p_rand.plot(kind="scatter", x="p1", y="success", color=colors[3], marker=markers[2], label="Only dissemination is restricted", ax=ax_hybrid)
conduct.plot(kind="scatter", x="p1", y="1_res_success", color=colors[5], marker=markers[3], label="Only conduct is restricted, 1 agent is limited", ax=ax_hybrid)
baseline.plot(kind="scatter", x="p1", y="success_complete", color=colors[7], marker=markers[1], label="No restrictions", ax=ax_hybrid)
ax_hybrid.set_xlabel("p")
ax_hybrid.set_ylabel("Number of trials that resulted in successful learning")
plt.savefig("hybrid.pdf")

# plt.show()
