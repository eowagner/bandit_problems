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