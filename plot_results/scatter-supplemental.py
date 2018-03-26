import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from numpy import linspace
import seaborn as sns

dirname = 'supplemental/'
dirnameOG = 'bernoulli-100k/'
total = 100000

markers = ["o", "+", "x", "^", "p", "d"]

colors = [sns.xkcd_rgb["pale red"]]

xkcdnames = ["windows blue", "amber", "greyish", "faded green", "dusty purple", "pale red"]
xkcdnames = ["windows blue", "dusty purple", "faded green", "amber", "greyish", "pale red"]
colors = [sns.xkcd_rgb[n] for n in xkcdnames]

plt.style.use('seaborn')

def normalize(df, col):
	df[col] = df[col]/total
	return df

agents_base = normalize(pd.read_csv(dirnameOG+'baseline-agents-6.csv', comment='#'), 'success_complete')
agents_base = agents_base.loc[agents_base['num_agents']>7]
conduct_base = normalize(pd.read_csv(dirnameOG+'conduct-agents-2.csv', comment='#'), 'success')
conduct_base = conduct_base.loc[conduct_base['num_agents']>7]
special_conduct = normalize(pd.read_csv(dirname+'special-conduct-agents-6.csv', comment='#'), 'success')
special_conduct = special_conduct.loc[special_conduct['num_agents']>7]

ax = conduct_base.plot(kind='scatter', x='num_agents', y='success', color=colors[0], marker=markers[0], label='Two restricted agents, DURC-style')
special_conduct.plot(kind='scatter', x='num_agents', y='success', color=colors[1], marker=markers[1], label='Referee\'s suggestion, One agent locked to arm A and another locked to arm B', ax=ax)
agents_base.plot(kind='scatter', x='num_agents', y='success_complete', color=colors[3], marker=markers[3], label='No restrictions', ax=ax)
ax.set_xlabel("Number of agents")
ax.set_ylabel("Probability of successful learning")
ax.set_title("Revise and Resubmit comparison, p = .6")
plt.savefig("figures/randr_agents.pdf")

p_base = normalize(pd.read_csv(dirnameOG+'baseline-p.csv', comment='#'), 'success_complete')
conduct_base = normalize(pd.read_csv(dirnameOG+'conduct-randomized.csv', comment='#'), '2_res_success')
special_conduct = normalize(pd.read_csv(dirname+'special-conduct-p.csv', comment='#'), 'success')

ax = conduct_base.plot(kind='scatter', x='p1', y='2_res_success', color=colors[0], marker=markers[0], label='Two restricted agents, DURC-style')
special_conduct.plot(kind='scatter', x='p1', y='success', color=colors[1], marker=markers[1], label="Referee\'s' suggestion", ax=ax)
p_base.plot(kind='scatter', x='p1', y='success_complete', color=colors[3], marker=markers[3], label='No restrictions', ax=ax)
ax.set_xlabel("p")
ax.set_ylabel("Probability of successful learning")
ax.set_title("Revise and Resubmit comparison, N=9")
plt.savefig("figures/randr_p.pdf")


p_wheel = normalize(pd.read_csv(dirname+'wheel-p.csv', comment='#'), 'success')
p_cycle_1 = normalize(pd.read_csv(dirname+'cycle-1-p.csv', comment='#'), 'success')
p_cycle_2 = normalize(pd.read_csv(dirname+'cycle-2-p.csv', comment='#'), 'success')
p_cycle_3 = normalize(pd.read_csv(dirname+'cycle-3-p.csv', comment='#'), 'success')
p_star = normalize(pd.read_csv(dirname+'star-p.csv', comment='#'), 'success')

ax = p_star.plot(kind='scatter', x='p1', y='success', color=colors[0], marker=markers[0], label='Star')
p_wheel.plot(kind='scatter', x='p1', y='success', color=colors[5], marker=markers[5], label='Wheel', ax=ax)
p_cycle_1.plot(kind='scatter', x='p1', y='success', color=colors[1], marker=markers[1], label='1-Cycle', ax=ax)
p_cycle_2.plot(kind='scatter', x='p1', y='success', color=colors[2], marker=markers[2], label='2-Cycle', ax=ax)
p_cycle_3.plot(kind='scatter', x='p1', y='success', color=colors[4], marker=markers[4], label='3-Cycle', ax=ax)
p_base.plot(kind='scatter', x='p1', y='success_complete', color=colors[3], marker=markers[3], label='No restrictions', ax=ax)
ax.set_xlabel("p")
ax.set_ylabel("Probability of successful learning")
ax.set_title("Alternative dissemination networks")
plt.savefig("figures/randr_alt_graphs.pdf")

exit()


ax_conduct_agents = conduct_agents_1.plot(kind="scatter", x="num_agents", y="success", color=colors[0], marker=markers[0], label="1 agent limited")
conduct_agents_2.plot(kind="scatter", x="num_agents", y="success", color=colors[1], marker=markers[1], label="2 agents limited", ax=ax_conduct_agents)
conduct_agents_3.plot(kind="scatter", x="num_agents", y="success", color=colors[2], marker=markers[2], label="3 agents limited", ax=ax_conduct_agents)
baseline_agents.plot(kind="scatter", x="num_agents", y="success_complete", color=colors[3], marker=markers[3], label="No restrictions", ax=ax_conduct_agents)
ax_conduct_agents.set_xlabel("Number of agents")
ax_conduct_agents.set_ylabel("Number of trials that resulted in successful learning")
ax_conduct_agents.set_title("Restricting Conduct, p = .6")
plt.savefig("conduct-agents.pdf")

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
plt.savefig("conduct.pdf")

ax_conduct_comp = conduct_rand.plot(kind="scatter", x="p1", y="1_res_success", color=colors[0], marker=markers[0], label="The DURC arm is chosen randomly")
conduct_low.plot(kind="scatter", x="p0", y="1_res_success", color=colors[1], marker=markers[1], label="The worse arm is the DURC arm", ax=ax_conduct_comp)
conduct_high.plot(kind="scatter", x="p1", y="1_res_success", color=colors[2], marker=markers[2], label="The bettter arm is the DURC arm", ax=ax_conduct_comp)
baseline.plot(kind="scatter", x="p1", y="success_complete", color=colors[3], marker=markers[3], label="No restrictions", ax=ax_conduct_comp)
ax_conduct_comp.set_xlabel("p")
ax_conduct_comp.set_ylabel("Number of trials that resulted in successful learning")
ax_conduct_comp.set_title("Restricting Conduct")
plt.savefig("conduct-comparison.pdf")

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
plt.savefig("combo.pdf")

ax_hybrid_comp = hybrid_rand.plot(kind="scatter", x="p1", y="1_res_success", color=colors[0], marker=markers[0], label="The dual-use arm is chosen randomly")
hybrid_low.plot(kind="scatter", x="p0", y="1_res_success", color=colors[1], marker=markers[1], label="The worse arm is the dual-use arm", ax=ax_hybrid_comp)
hybrid_high.plot(kind="scatter", x="p1", y="1_res_success", color=colors[2], marker=markers[2], label="The better arm is the dual-use arm", ax=ax_hybrid_comp)
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

#time data
baseline['time_succ_complete'] = baseline['time_succ_complete']/baseline['success_complete']
diss_p_rand['success_time'] = diss_p_rand['success_time']/diss_p_rand['success']
conduct_rand['1_res_succ_time'] = conduct_rand['1_res_succ_time']/conduct_rand['1_res_success']
hybrid_rand['1_res_succ_time'] = hybrid_rand['1_res_succ_time']/hybrid_rand['1_res_success']

# baseline['time_succ_complete'] = baseline['time_succ_complete'].apply(lambda x: x/100000)
# diss_p_rand['success_time'] = diss_p_rand['success_time'].apply(lambda x: x/100000)
# conduct_rand['1_res_succ_time'] = conduct_rand['1_res_succ_time'].apply(lambda x: x/100000)
# hybrid_rand['1_res_succ_time'] = hybrid_rand['1_res_succ_time'].apply(lambda x: x/100000)

# ax_time = baseline.plot(kind="scatter", x="p1", y="time_star", color=colors[0], marker=markers[0], label="Star graph -- baseline")
ax_time = diss_p_rand.plot(kind="scatter", x="p1", y="success_time", color=colors[0], marker=markers[0], label="Dissemination restricted")
conduct_rand.plot(kind="scatter", x="p1", y="1_res_succ_time", color=colors[1], marker=markers[1], label="Conduct restricted", ax=ax_time)
hybrid_rand.plot(kind="scatter", x="p1", y="1_res_succ_time", color=colors[2], marker=markers[2], label="Both restricted", ax=ax_time)
baseline.plot(kind="scatter", x="p1", y="time_succ_complete", color=colors[3], marker=markers[3], label="No restrictions", ax=ax_time)
ax_time.set_xlabel("p")
ax_time.set_ylabel("Mean Time to fixing on the correct arm")
ax_time.set_title("Mean number of steps until fixing on the correct arm")
plt.savefig("time.pdf")

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

# d6 = pivot(conduct_rand, baseline, .6)
# d7 = pivot(conduct_rand, baseline, .7)
# d8 = pivot(conduct_rand, baseline, .8)

# ax_conduct_combined = d6.plot(kind="scatter", x="num_agents_restricted", color=colors[0], marker=markers[0], y="success")
# d7.plot(kind="scatter", x="num_agents_restricted", y="success", color=colors[-1], marker=markers[1], ax=ax_conduct_combined)
# d8.plot(kind="scatter", x="num_agents_restricted", y="success", color=colors[2], marker=markers[2], ax=ax_conduct_combined)
# plt.savefig("conduct-arms.pdf")