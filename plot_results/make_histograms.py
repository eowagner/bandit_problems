import pandas
import matplotlib.pyplot as plt
from matplotlib import cm
from numpy import linspace
import seaborn as sns
import numpy

dirname = 'bernoulli-10k/'


xkcdnames = ["windows blue", "amber", "greyish", "faded green", "dusty purple"]
xkcdnames = ["windows blue", "dusty purple", "faded green", "amber", "greyish"]
colors = [sns.xkcd_rgb[n] for n in xkcdnames]

plt.style.use('seaborn')

df = pandas.read_csv(dirname + 'time.csv', comment="#")

df = df.drop('index', axis=1)

print(df.describe())

diss_s = df['diss_success_time'].values
comp_s = df[df.complete_success_time.notnull()]['complete_success_time'].values

y_lim = 8000


fig, (ax1, ax2) = plt.subplots(ncols=2, sharey=True)
# plt.suptitle("Steps until settling on the correct arm")
sns.distplot(diss_s, kde=False, ax=ax1, color="b")
ax1.set_xlabel('Steps until settling on the correct arm')
ax1.set_ylabel('Number of trials')
ax1.set_title("Restricing Dissemination")

sns.distplot(comp_s, kde=False, ax=ax2, color="b")
ax2.set_title("No Restrictions")
ax1.set_ylabel('Number of trials')
ax2.set_xlabel('Steps until settling on the correct arm')
# plt.show()
plt.savefig("histograms.pdf")

#Histogram zoomed in for simulations that locked before step n
n = 100
diss_s_t = diss_s[diss_s < n]
comp_s_t = comp_s[comp_s < n]

plt.figure()
# plt.suptitle("Steps until settling on the correct arm")
a = sns.distplot(diss_s_t, kde=False, color=colors[0], label="Restricting dissemination", hist_kws=dict(cumulative=True, edgecolor='black', linewidth=1.2), kde_kws=dict(cumulative=True))
a.set_xlabel('Steps until settling on the correct arm')
a.set_ylabel('Number of trials')

sns.distplot(comp_s_t, kde=False, color=colors[3], ax=a, label="No restrictions", hist_kws=dict(cumulative=True, edgecolor='black', linewidth=1.2), kde_kws=dict(cumulative=True))
plt.legend()
# plt.show()
plt.savefig("cumulative_histograms.pdf")


def print_table(a, b):
	for n in range(1,50,1):
		print("Less than {2}:\t {0} \t {1}".format(a[a<n].count(), b[b<n].count(), n))

df_succ = df['diss_success_time']
df_comp = df['complete_success_time']

print_table(df_succ, df_comp)