import pandas
import matplotlib.pyplot as plt
from matplotlib import cm
from numpy import linspace
import seaborn as sns

dirname = 'bernoulli-10k/'

start = 0.0
stop = 1.0
number_of_colors= 8
cm_subsection = linspace(start, stop, number_of_colors) 
circular_colors = [ cm.jet(x) for x in cm_subsection ]

markers = ["o", "+", "x", "^"]

colors = [sns.xkcd_rgb["pale red"]]

xkcdnames = ["windows blue", "amber", "greyish", "faded green", "dusty purple"]
xkcdnames = ["windows blue", "dusty purple", "faded green", "amber", "greyish"]
colors = [sns.xkcd_rgb[n] for n in xkcdnames]

plt.style.use('seaborn')

baseline = pandas.read_csv(dirname + 'baseline-p.csv', comment="#")
baseline_agents = pandas.read_csv(dirname + 'baseline-agents-6.csv', comment="#")

diss_p_rand = pandas.read_csv(dirname + 'diss-p-randomized.csv', comment="#")
diss_p_low = pandas.read_csv(dirname + 'diss-p-low.csv', comment="#")
diss_p_high = pandas.read_csv(dirname + 'diss-p-high.csv', comment="#")

diss_agents_rand = pandas.read_csv(dirname + 'diss-agents-6-randomized.csv', comment="#")
diss_agents_low = pandas.read_csv(dirname + 'diss-agents-6-low.csv', comment="#")
diss_agents_high = pandas.read_csv(dirname + 'diss-agents-6-high.csv', comment="#")

conduct_rand = pandas.read_csv(dirname + 'conduct-randomized.csv', comment="#")
conduct_low = pandas.read_csv(dirname + 'conduct-low.csv', comment="#")
conduct_high = pandas.read_csv(dirname + 'conduct-high.csv', comment="#")

hybrid_rand = pandas.read_csv(dirname + 'hybrid-randomized.csv', comment="#")
hybrid_low = pandas.read_csv(dirname + 'hybrid-low.csv', comment="#")
hybrid_high = pandas.read_csv(dirname + 'hybrid-high.csv', comment="#")

ax_baseline = baseline.plot(kind="scatter", x="p1", y="success_star", color=colors[0], marker=markers[0], label="Star graph")
baseline.plot(kind="scatter", x="p1", y="success_complete", label="Complete graph", color=colors[1], marker=markers[1], ax=ax_baseline)
ax_baseline.set_xlabel("p")
ax_baseline.set_ylabel("Number of trials that resulted in successful learning")
ax_baseline.set_title("Baseline comparison")
plt.savefig("baseline.pdf")

ax_baseline_agents = baseline_agents.plot(kind="scatter", x="num_agents", y="success_star", color=colors[0], marker=markers[0], label="Star graph")
baseline_agents.plot(kind="scatter", x="num_agents", y="success_complete", color=colors[1], marker=markers[1], label="Complete graph", ax=ax_baseline_agents)
ax_baseline_agents.set_xlabel("Number of agents")
ax_baseline_agents.set_ylabel("Number of trials that resulted in successful learning")
ax_baseline_agents.set_title("Baseline comparison agents")
plt.savefig("baseline-agents.pdf")

ax_diss = diss_p_rand.plot(kind="scatter", x="p1", y="success", color=colors[0], marker=markers[0], label="A random arm's dissemination is restricted")
diss_p_low.plot(kind="scatter", x="p1", y="success", color=colors[1], marker=markers[1], label="The worse arm's dissemination is restricted", ax=ax_diss)
diss_p_high.plot(kind="scatter", x="p1", y="success", color=colors[2], marker=markers[2], label="The better arm's dissemination is restricted", ax=ax_diss)
baseline.plot(kind="scatter", x="p1", y="success_complete", color=colors[3], marker=markers[3], label="No restrictions", ax=ax_diss)
ax_diss.set_xlabel("p")
ax_diss.set_ylabel("Number of trials that resulted in successful learning")
ax_diss.set_title("Restricting Dissemination")
plt.savefig("dissemination.pdf")

ax_diss_agents = diss_agents_rand.plot(kind="scatter", x="num_agents", y="success", color=colors[0], marker=markers[0], label="A random arm's dissemination is restriced")
diss_agents_low.plot(kind="scatter", x="num_agents", y="success", color=colors[1], marker=markers[1], label="The worse arm's dissemination is restricted", ax=ax_diss_agents)
diss_agents_high.plot(kind="scatter", x="num_agents", y="success", color=colors[2], marker=markers[2], label="The better arm's dissemination restricted", ax=ax_diss_agents)
baseline_agents.plot(kind="scatter", x="num_agents", y="success_complete", color=colors[3], marker=markers[3], label="No restrictions", ax=ax_diss_agents)
ax_diss_agents.set_xlabel("Number of agents")
ax_diss_agents.set_ylabel("Number of trials that resulted in successful learning")
ax_diss_agents.set_title("Restricting Dissemination")
plt.savefig("diss-agents.pdf")

ax_conduct_rand = conduct_rand.plot(kind="scatter", x="p1", y="1_res_success", color=circular_colors[0], label="7 DURC agents")
conduct_rand.plot(kind="scatter", x="p1", y="2_res_success", color=circular_colors[1], label="6 DURC agents", ax=ax_conduct_rand)
conduct_rand.plot(kind="scatter", x="p1", y="3_res_success", color=circular_colors[2], label="5 DURC agents", ax=ax_conduct_rand)
conduct_rand.plot(kind="scatter", x="p1", y="4_res_success", color=circular_colors[3], label="4 DURC agents", ax=ax_conduct_rand)
conduct_rand.plot(kind="scatter", x="p1", y="5_res_success", color=circular_colors[4], label="3 DURC agents", ax=ax_conduct_rand)
conduct_rand.plot(kind="scatter", x="p1", y="6_res_success", color=circular_colors[5], label="2 DURC agents", ax=ax_conduct_rand)
conduct_rand.plot(kind="scatter", x="p1", y="7_res_success", color=circular_colors[6], label="1 DURC agent", ax=ax_conduct_rand)
baseline.plot(kind="scatter", x="p1", y="success_complete", color=circular_colors[7], label="No restrictions", ax=ax_conduct_rand)
ax_conduct_rand.set_xlabel("p")
ax_conduct_rand.set_ylabel("Number of trials that resulted in successful learning")
ax_conduct_rand.set_title("Restricting Conduct")
plt.savefig("conduct.pdf")

ax_conduct_comp = conduct_rand.plot(kind="scatter", x="p1", y="1_res_success", color=colors[0], marker=markers[0], label="The DURC arm is chosen randomly")
conduct_low.plot(kind="scatter", x="p0", y="1_res_success", color=colors[1], marker=markers[1], label="The worse arm is the DURC arm", ax=ax_conduct_comp)
conduct_high.plot(kind="scatter", x="p1", y="1_res_success", color=colors[2], marker=markers[2], label="The bettter arm is the DURC arm", ax=ax_conduct_comp)
baseline.plot(kind="scatter", x="p1", y="success_complete", color=colors[3], marker=markers[3], label="No restrictions", ax=ax_conduct_comp)
ax_conduct_comp.set_xlabel("p")
ax_conduct_comp.set_ylabel("Number of trials that resulted in successful learning")
ax_conduct_comp.set_title("Restricting Conduct")
plt.savefig("conduct-comparison.pdf")

ax_hybrid_rand = hybrid_rand.plot(kind="scatter", x="p1", y="1_res_success", color=circular_colors[0], label="7 DURC agents")
hybrid_rand.plot(kind="scatter", x="p1", y="2_res_success", color=circular_colors[1], label="6 DURC agents", ax=ax_hybrid_rand)
hybrid_rand.plot(kind="scatter", x="p1", y="3_res_success", color=circular_colors[2], label="5 DURC agents", ax=ax_hybrid_rand)
hybrid_rand.plot(kind="scatter", x="p1", y="4_res_success", color=circular_colors[3], label="4 DURC agents", ax=ax_hybrid_rand)
hybrid_rand.plot(kind="scatter", x="p1", y="5_res_success", color=circular_colors[4], label="3 DURC agents", ax=ax_hybrid_rand)
hybrid_rand.plot(kind="scatter", x="p1", y="6_res_success", color=circular_colors[5], label="2 DURC agents", ax=ax_hybrid_rand)
hybrid_rand.plot(kind="scatter", x="p1", y="7_res_success", color=circular_colors[6], label="1 DURC agent", ax=ax_hybrid_rand)
baseline.plot(kind="scatter", x="p1", y="success_complete", color=circular_colors[7], label="No restrictions", ax=ax_hybrid_rand)
ax_hybrid_rand.set_xlabel("p")
ax_hybrid_rand.set_ylabel("Number of trials that resulted in successful learning")
ax_hybrid_rand.set_title("Restricting both Dissemination and Conduct")
plt.savefig("combo.pdf")

ax_hybrid_comp = hybrid_rand.plot(kind="scatter", x="p1", y="1_res_success", color=colors[0], marker=markers[0], label="The DURC arm is chosen randomly")
hybrid_low.plot(kind="scatter", x="p0", y="1_res_success", color=colors[1], marker=markers[1], label="The worse arm is the DURC arm", ax=ax_hybrid_comp)
hybrid_high.plot(kind="scatter", x="p1", y="1_res_success", color=colors[2], marker=markers[2], label="The better arm is the DURC arm", ax=ax_hybrid_comp)
baseline.plot(kind="scatter", x="p1", y="success_complete", color=colors[3], marker=markers[3], label="No restrictions", ax=ax_hybrid_comp)
ax_hybrid_comp.set_xlabel("p")
ax_hybrid_comp.set_ylabel("Number of trials that resulted in successful learning")
ax_hybrid_comp.set_title("Restricting both Dissemination and Conduct")
plt.savefig("combo-comparison.pdf")

ax_reg_comp = hybrid_rand.plot(kind="scatter", x="p1", y="1_res_success", color=colors[0], marker=markers[0], label="Both conduct and dissemination are restricted")
diss_p_rand.plot(kind="scatter", x="p1", y="success", label="Only dissemination is restricted", color=colors[1], marker=markers[1], ax=ax_reg_comp)
conduct_rand.plot(kind="scatter", x="p1", y="1_res_success", label="Only conduct is restricted", color=colors[2], marker=markers[2], ax=ax_reg_comp)
baseline.plot(kind="scatter", x="p1", y="success_complete", label="No restrictions", color=colors[3], marker=markers[3], ax=ax_reg_comp)
ax_reg_comp.set_xlabel("p")
ax_reg_comp.set_ylabel("Number of trials that resulted in successful learning")
ax_reg_comp.set_title("Comparing Regulatory Schemes")
plt.savefig("regulations-comp.pdf")

def pivot(data, base, p):
	fuzz = .001
	row = data.loc[(data["p1"] >= p-fuzz) & (data["p1"] <= p+fuzz)]
	rowb = base.loc[(data["p1"] >= p-fuzz) & (data["p1"] <= p+fuzz)]

	row = row.transpose()
	row = row[3:10]
	row.columns = ['success']
	row['num_agents_restricted'] = range(1,8)

	# rowb = pandas.DataFrame({'success' : [rowb.at[19,'success_complete']], 'num_agents_restricted': [0]})
	rowb = pandas.DataFrame({'success' : [rowb['success_complete'].tolist()[0]], 'num_agents_restricted': [0]})

	return row.append(rowb)

d6 = pivot(conduct_rand, baseline, .6)
d7 = pivot(conduct_rand, baseline, .7)
d8 = pivot(conduct_rand, baseline, .8)

# ax_conduct_combined = d6.plot(kind="scatter", x="num_agents_restricted", color=colors[0], marker=markers[0], y="success")
# d7.plot(kind="scatter", x="num_agents_restricted", y="success", color=colors[-1], marker=markers[1], ax=ax_conduct_combined)
# d8.plot(kind="scatter", x="num_agents_restricted", y="success", color=colors[2], marker=markers[2], ax=ax_conduct_combined)
# plt.savefig("conduct-arms.pdf")