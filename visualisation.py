from github import Github
import requests
#from pprint import pprint
from githubAPI import *
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

g = Github()

try:
	tokentext = open("token.txt")
except FileNotFoundError:
	print("Token file not found.")
	username = input("Enter GitHub username: ")
	user = g.get_user(username)	
else:
    token = tokentext.readline()
    g = Github(token)
    user = g.get_user()
    
repoData = repoToData(user)

data = pd.DataFrame.from_dict(repoData, orient = 'index', columns = ["Repository Name", "Programming language", 
"Date created", "Date Last Pushed", "Repo Commits", "Star Count"])

starCount = data.sort_values(by = ['Star Count'], ascending = False)
plot = sns.barplot(data = starCount[0:5], x = 'Repository Name', y = 'Star Count', palette = 'bright')
plot.set_title(user.login + " Repository Star Count")

plt.show()

numberOfCommits = data.sort_values(by = ['Repo Commits'], ascending = True)
plot = sns.barplot(data = numberOfCommits[0:10], x = 'Repo Commits', y = 'Repository Name', palette = 'mako')
plot.set_title(user.login + " Repository Commits")

plt.show()
