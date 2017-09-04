import pandas
import matplotlib.pyplot as plt


df_p_uniform = pandas.read_csv('baseline/10k-p-uniform.csv', comment="#")
df_p_random = pandas.read_csv('baseline/10k-p-random.csv', comment="#")
df_p_jeffrey = pandas.read_csv('baseline/10k-p-jeffrey.csv', comment="#")
# df_p_random_si = pandas.read_csv('1k-p-random-smallinterval.csv', comment="#")

axP = df_p_uniform.plot(kind="scatter", x="p1", y="success_complete", color="r", label="Complete graph, uniform priors")
df_p_uniform.plot(kind="scatter", x="p1", y="success_star", color="b", label="Star graph, uniform priors", ax=axP)
df_p_random.plot(kind="scatter", x="p1", y="success_complete", color="y", label="Complete graph, random priors", ax=axP)
df_p_random.plot(kind="scatter", x="p1", y="success_star", color="g", label="Star graph, random priors", ax=axP)
df_p_jeffrey.plot(kind="scatter", x="p1", y="success_complete", color="k", label="Complete graph, jeffrey priors", ax=axP)
df_p_jeffrey.plot(kind="scatter", x="p1", y="success_star", color="k", label="Star graph, jeffrey priors", ax=axP)


df_agents_uniform = pandas.read_csv('baseline/10k-agents-uniform.csv', comment="#")

axA = df_agents_uniform.plot(kind="scatter", x="num_agents", y="success_complete", color="r", label="Complete graph, uniform priors")
df_agents_uniform.plot(kind="scatter", x="num_agents", y="success_star", color="b", label="Star graph, uniform priors", ax=axA)


plt.show()

