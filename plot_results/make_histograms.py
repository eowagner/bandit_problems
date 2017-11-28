import pandas
import matplotlib.pyplot as plt
from matplotlib import cm
from numpy import linspace
import seaborn as sns
import numpy

dirname = 'bernoulli-100k/'


xkcdnames = ["windows blue", "amber", "greyish", "faded green", "dusty purple"]
xkcdnames = ["windows blue", "dusty purple", "faded green", "amber", "greyish"]
colors = [sns.xkcd_rgb[n] for n in xkcdnames]

plt.style.use('seaborn')

def print_table(a, b, c, d):
	for n in range(1,20,1):
		print("Less than {}:\t {} \t {} \t {} \t {}".format(n, a[a<n].count(), b[b<n].count(), c[c<n].count(), d[d<n].count()))

def makefigures(p):
	df = pandas.read_csv(dirname + 'time-' + str(p) + '.csv', comment="#")
	df = df.drop('index', axis=1)

	print(df.describe())

	diss_s = df[df.diss_succ.notnull()]['diss_succ'].values
	comp_s = df[df.comp_succ.notnull()]['comp_succ'].values
	cond_s = df[df.cond_succ.notnull()]['cond_succ'].values
	hybrid_s = df[df.hybrid_succ.notnull()]['hybrid_succ'].values

	#Histogram zoomed in for simulations that locked before step n, Restricting Dissemination
	n = 100
	diss_s = diss_s[diss_s < n]
	comp_s = comp_s[comp_s < n]

	plt.figure()
	# plt.suptitle("Steps until settling on the correct arm")
	a = sns.distplot(diss_s, kde=False, color=colors[0], label="Restricting dissemination", hist_kws=dict(cumulative=True, edgecolor='black', linewidth=1.2), kde_kws=dict(cumulative=True))
	a.set_xlabel('Steps')
	a.set_ylabel('Number of simulations that have fixed on the best arm')
	a.set_title('Restricting Dissemination, p=.' + str(p))
	# plt.ylim([10000,100000])

	sns.distplot(comp_s, kde=False, color=colors[3], ax=a, label="No restrictions", hist_kws=dict(cumulative=True, edgecolor='black', linewidth=1.2), kde_kws=dict(cumulative=True))
	plt.legend()
	# plt.show()
	plt.savefig("cumulative_diss-" + str(p) + ".pdf")

	#Cumulative Histogram for conduct
	cond_s = cond_s[cond_s < n]

	plt.figure()
	# plt.suptitle("Steps until settling on the correct arm")
	a = sns.distplot(cond_s, kde=False, color=colors[0], label="Restricting Conduct", hist_kws=dict(cumulative=True, edgecolor='black', linewidth=1.2), kde_kws=dict(cumulative=True))
	a.set_xlabel('Steps')
	a.set_ylabel('Number of simulations that have fixed on the best arm')
	a.set_title('Restricting Conduct, p=.' + str(p))
	# plt.ylim([10000,100000])

	sns.distplot(comp_s, kde=False, color=colors[3], ax=a, label="No restrictions", hist_kws=dict(cumulative=True, edgecolor='black', linewidth=1.2), kde_kws=dict(cumulative=True))
	plt.legend()
	# plt.show()
	plt.savefig("cumulative_cond-" + str(p) + ".pdf")

	#Cumulative Histogram for hybrid
	hybrid_s = hybrid_s[hybrid_s < n]

	plt.figure()
	# plt.suptitle("Steps until settling on the correct arm")
	a = sns.distplot(hybrid_s, kde=False, color=colors[0], label="Restricting both Dissemination and Conduct", hist_kws=dict(cumulative=True, edgecolor='black', linewidth=1.2), kde_kws=dict(cumulative=True))
	a.set_xlabel('Steps')
	a.set_ylabel('Number of simulations that have fixed on the best arm')
	a.set_title('Restricting both Dissemination and Conduct, p=.' + str(p))
	# plt.ylim([10000,100000])

	sns.distplot(comp_s, kde=False, color=colors[3], ax=a, label="No restrictions", hist_kws=dict(cumulative=True, edgecolor='black', linewidth=1.2), kde_kws=dict(cumulative=True))
	plt.legend()
	# plt.show()
	plt.savefig("cumulative_hybrid-" + str(p) + ".pdf")

	# Print the cumulative table
	print("\n\n\t\tComp\tDiss\tCond\tHybrid")
	print_table(df['comp_succ'], df['diss_succ'], df['cond_succ'], df['hybrid_succ'])

print("p=.55 ################################")
makefigures(55)

print("p=.6 ################################")
makefigures(6)

print("p=.8 ################################")
makefigures(8)