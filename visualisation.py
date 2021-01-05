from github import Github
import requests
from pprint import pprint
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
	#print(getUserRepos(user))
else:
    token = tokentext.readline()
    g = Github(token)
    user = g.get_user()
	#print(getTokenRepos(g))
    
#print(getUserRepos(user))

repoData = repoToData(user)

data = pd.DataFrame.from_dict(repoData, orient = 'index', columns = ["Repository Name", "Programming language", 
"Date created", "Date Last Pushed", "Star Count"])

starCount = data.sort_values(by=['Star Count'], ascending=False)
plot = sns.barplot(data = starCount[0:5], x='Repository Name', y='Star Count', palette='tab10')
plot.set_title("Star Count")

plt.show()
