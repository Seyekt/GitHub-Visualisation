from github import Github
import requests
from pprint import pprint
from githubAPI import *
import seaborn as sns
import matplotlib.pyplot as plt

g = Github()

try:
	tokentext = open("token.txt")
except FileNotFoundError:
	print("Token file not found.")
	username = input("Enter GitHub username: ")
	user = g.get_user(username)	
	#print(getUserRepos(user))
else:
    token = tokentext.readline()
    g = Github(token)
    user = g.get_user()
	#print(getTokenRepos(g))
    
print(getUserRepos(user))

# Load an example dataset
tips = sns.load_dataset("tips")
repoData = repoToData(user)

sns.set_theme()

# Create a visualization
sns.relplot (
    data=repoData,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size",
)

plt.show()