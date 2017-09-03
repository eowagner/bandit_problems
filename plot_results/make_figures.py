import pandas
import matplotlib.pyplot as plt


df_p_uniform = pandas.read_csv('1k-p-uniform.csv', comment="#")
df_p_random = pandas.read_csv('1k-p-random.csv', comment="#")
df_p_random_si = pandas.read_csv('1k-p-random-smallinterval.csv', comment="#")

axP = df_p_uniform.plot(kind="scatter", x="p1", y="success_complete", color="r", label="Complete graph, uniform priors")
df_p_uniform.plot(kind="scatter", x="p1", y="success_star", color="b", label="Star graph, uniform priors", ax=axP)
df_p_random.plot(kind="scatter", x="p1", y="success_star", color="g", label="Star graph, random priors", ax=axP)
df_p_random.plot(kind="scatter", x="p1", y="success_complete", color="y", label="Complete graph, random priors", ax=axP)

axR = df_p_random.plot(kind="scatter", x="p1", y="success_complete", color="y", label="Complete graph, random priors")
df_p_random_si.plot(kind="scatter", x="p1", y="success_complete", color="b", label="Complete graph, random priors, small interval", ax=axR)
df_p_uniform.plot(kind="scatter", x="p1", y="success_complete", color="r", label="Complete graph, uniform priors", ax=axR)

df_agents_uniform = pandas.read_csv('1k-agents-uniform.csv', comment="#")

axA = df_agents_uniform.plot(kind="scatter", x="num_agents", y="success_complete", color="r", label="Complete graph, uniform priors")
df_agents_uniform.plot(kind="scatter", x="num_agents", y="success_star", color="b", label="Star graph, uniform priors", ax=axA)


plt.show()

# df = pandas.read_csv('baseline-100k.csv', comment="#")

# # print(df)

# axU = df.plot(kind="scatter", x="p", y="uniform_complete_success", color="r", label="Uniform priors, Complete graph")
# df.plot(kind="scatter", x="p", y="uniform_star_success", color="b", label="Uniform priors, Star graph", ax=axU)

# axJ = df.plot(kind="scatter", x="p", y="jeffrey_complete_success", color="r", label="Jeffrey priors, Complete graph")
# df.plot(kind="scatter", x="p", y="jeffrey_star_success", color="b", label="Jeffrey priors, Star graph", ax=axJ)

# axR = df.plot(kind="scatter", x="p", y="random_complete_success", color="r", label="Random priors, Complete graph")
# df.plot(kind="scatter", x="p", y="random_star_success", color="b", label="Random priors, Star graph", ax=axR)

# axPriors = df.plot(kind="scatter", x="p", y="uniform_complete_success", color="r", label="Uniform priors")
# df.plot(kind="scatter", x="p", y="jeffrey_complete_success", color="b", label="Jeffrey priors", ax=axPriors)
# df.plot(kind="scatter", x="p", y="random_complete_success", color="g", label="Random priors", ax=axPriors)

# plt.show()

# ax = df.plot(kind="scatter", x="p", y="succ_complete", color="r", label="Complete")
# df.plot(kind="scatter", x="p", y="succ_cycle", color="b", label="Cycle", ax=ax)

# dfComplete = pandas.read_csv('complete.csv', comment="#")
# dfCycle = pandas.read_csv('cycle.csv', comment="#")


# ax = dfComplete.plot(kind='scatter', x='p', y='succ_count', color='r')

# dfCycle.plot(kind='scatter', x='p', y='succ_count', color='g', ax=ax)

# plt.show() 

