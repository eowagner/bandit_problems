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

df = pandas.read_csv('time.csv', comment="#")

df = df.drop('index', axis=1)

print(df.describe())

diss_s = df['diss_success_time'].values
comp_s = df[df.complete_success_time.notnull()]['complete_success_time'].values

y_lim = 8000

# sns.distplot(dst, kde=False, rug=True) the program appears to freeze when producing a rug.  Too many data points?
# ax = sns.distplot(diss_s, kde=False)
# ax.set(ylim=(0, y_lim))
# plt.show()

# ax = sns.distplot(comp_s, kde=False)
# ax.set(ylim=(0, y_lim))
# plt.show()

fig, (ax1, ax2) = plt.subplots(ncols=2, sharey=True)
# plt.suptitle("Steps until settling on the correct arm")

sns.distplot(diss_s, kde=False, ax=ax1, color="b")
ax1.set_xlabel('Steps until settling on the correct arm')
ax1.set_ylabel('Number of simulations')
ax1.set_title("Restricing Dissemination")

sns.distplot(comp_s, kde=False, ax=ax2, color="b")
ax2.set_title("No Restrictions")
ax2.set_xlabel('Steps until settling on the correct arm')
plt.show()

# no1 = df['diss_success_time'] < 750
# print(df[no1].describe())

# plt.figure()
# df['diss_success_time'].plot.hist(bins=100, cumulative=True, label="Restricted dissemination, success")
# df['complete_success_time'].plot.hist(bins=100, cumulative=True, label="No restrictions, success")

# df['diss_success_time'].plot.hist(bins=50, label="Restricted dissemination, success")
# df['complete_success_time'].plot.hist(bins=50, label="No restrictions, success")

# df.hist(bins=50)
# plt.show()

