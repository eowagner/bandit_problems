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

baseline = pandas.read_csv(dirname + 'baseline-p-uniform.csv', comment="#")
baseline_agents = pandas.read_csv(dirname + 'baseline-agents-uniform-55.csv', comment="#")
# baseline_agents_b = pandas.read_csv(dirname + 'baseline-agents-uniform-6.csv', comment="#")
dissemination = pandas.read_csv(dirname + 'diss-p-uniform.csv', comment="#")
dissemination_agents = pandas.read_csv(dirname + 'diss-agents-uniform-55.csv', comment="#")
conduct = pandas.read_csv(dirname + 'conduct-p-uniform.csv', comment="#")

ax_baseline = baseline.plot(kind="scatter", x="p1", y="success_complete", color=colors[0], label="Complete graph")
baseline.plot(kind="scatter", x="p1", y="success_star", label="Star graph", color=colors[1], ax=ax_baseline)

ax_baseline_agents = baseline_agents.plot(kind="scatter", x="num_agents", y="success_complete", color=colors[0], label="Complete graph")
baseline_agents.plot(kind="scatter", x="num_agents", y="success_star", color=colors[1], label="Star graph", ax=ax_baseline_agents)

ax_dissemination = dissemination.plot(kind="scatter", x="p1", y="success", color=colors[1], label="Restricted dissemination")
baseline.plot(kind="scatter", x="p1", y="success_complete", color=colors[0], label="No restrictions", ax=ax_dissemination)
dissemination.plot(kind="scatter", x="p1", y="consensus", color=colors[2], label="Consensus", ax=ax_dissemination)

ax_dissemination_agents = dissemination_agents.plot(kind="scatter", x="num_agents", y="success", color=colors[1], label="Restricted dissemination")
baseline_agents.plot(kind="scatter", x="num_agents", y="success_complete", color=colors[0], label="No restrictions", ax=ax_dissemination_agents)
# dissemination_agents.plot(kind="scatter", x="num_agents", y="consensus", color=colors[2], label="Restricted dissemination", ax=ax_dissemination_agents)

ax_conduct = conduct.plot(kind="scatter", x="p1", y="1_res_success", color=colors[0], label="1 restricted agent")
conduct.plot(kind="scatter", x="p1", y="2_res_success", color=colors[1], label="2 restricted agents", ax=ax_conduct)
conduct.plot(kind="scatter", x="p1", y="3_res_success", color=colors[2], label="3 restricted agents", ax=ax_conduct)
conduct.plot(kind="scatter", x="p1", y="4_res_success", color=colors[3], label="4 restricted agents", ax=ax_conduct)
conduct.plot(kind="scatter", x="p1", y="5_res_success", color=colors[4], label="5 restricted agents", ax=ax_conduct)
conduct.plot(kind="scatter", x="p1", y="6_res_success", color=colors[5], label="6 restricted agents", ax=ax_conduct)
conduct.plot(kind="scatter", x="p1", y="7_res_success", color=colors[6], label="7 restricted agents", ax=ax_conduct)
baseline.plot(kind="scatter", x="p1", y="success_complete", color=colors[7], label="No restrictions", ax=ax_conduct)


plt.show()

