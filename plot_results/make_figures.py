import pandas
import matplotlib.pyplot as plt


baseline_p_uniform = pandas.read_csv('baseline/10k-p-uniform.csv', comment="#")
baseline_p_random = pandas.read_csv('baseline/10k-p-random.csv', comment="#")
baseline_p_jeffrey = pandas.read_csv('baseline/10k-p-jeffrey.csv', comment="#")

dissemination_p_uniform = pandas.read_csv('dissemination/1k-p-uniform.csv', comment="#")


axP = baseline_p_uniform.plot(kind="scatter", x="p1", y="success_complete", color="r", label="Complete graph, uniform priors")
baseline_p_uniform.plot(kind="scatter", x="p1", y="success_star", color="b", label="Star graph, uniform priors", ax=axP)
baseline_p_random.plot(kind="scatter", x="p1", y="success_complete", color="y", label="Complete graph, random priors", ax=axP)
baseline_p_random.plot(kind="scatter", x="p1", y="success_star", color="g", label="Star graph, random priors", ax=axP)
baseline_p_jeffrey.plot(kind="scatter", x="p1", y="success_complete", color="k", label="Complete graph, jeffrey priors", ax=axP)
baseline_p_jeffrey.plot(kind="scatter", x="p1", y="success_star", color="k", label="Star graph, jeffrey priors", ax=axP)


ax_dissemination = baseline_p_uniform.plot(kind="scatter", x="p1", y="success_complete", color="r", label="No restrictions")
dissemination_p_uniform.plot(kind="scatter", x="p1", y="success", color="b", label="Restrictions on one arm", ax=ax_dissemination)
baseline_p_uniform.plot(kind="scatter", x="p1", y="success_star", color="g", label="Restrictions on both arms", ax=ax_dissemination)

df_agents_uniform = pandas.read_csv('baseline/10k-agents-uniform.csv', comment="#")

axA = df_agents_uniform.plot(kind="scatter", x="num_agents", y="success_complete", color="r", label="Complete graph, uniform priors")
df_agents_uniform.plot(kind="scatter", x="num_agents", y="success_star", color="b", label="Star graph, uniform priors", ax=axA)


plt.show()

