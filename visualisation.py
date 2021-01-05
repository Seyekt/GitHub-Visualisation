from github import Github
import requests
from pprint import pprint
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

# Load an example dataset
tips = sns.load_dataset("tips")

# Create a visualization
sns.relplot (
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size",
)

plt.show()