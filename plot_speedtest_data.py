import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("speedtest_data.csv")

sns.relplot(x="connections", y="execution_time", data=df, kind="line", markers=True)
plt.xscale("log")
plt.xlabel("Number of Connections")
plt.ylabel("Execution Time (s)")
plt.title("Wall time to run GPQA diamond on GPT-4o")
plt.show()