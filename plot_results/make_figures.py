import pandas
import matplotlib.pyplot as plt


df = pandas.read_csv('baseline.csv', comment="#")

ax = df.plot(kind="scatter", x="p", y="succ_complete", color="r", label="Complete")
df.plot(kind="scatter", x="p", y="succ_cycle", color="b", label="Cycle", ax=ax)

# dfComplete = pandas.read_csv('complete.csv', comment="#")
# dfCycle = pandas.read_csv('cycle.csv', comment="#")


# ax = dfComplete.plot(kind='scatter', x='p', y='succ_count', color='r')

# dfCycle.plot(kind='scatter', x='p', y='succ_count', color='g', ax=ax)

plt.show() 

