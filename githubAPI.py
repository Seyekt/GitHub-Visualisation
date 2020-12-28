from github import Github
import requests
from pprint import pprint

def getUserData(username):
	url = f"https://api.github.com/users/{username}"
	userData = requests.get(url).json()
	return userData

def repoToStr(repo):
	output = ""
	output += ("Repository Name: " + repo.full_name + "\n")
	output += ("Description: " + str(repo.description) + "\n")
	output += ("Programming language: " + str(repo.language) + "\n")
	output += ("Date created: " + str(repo.created_at) + "\n") 
	output += ("Date Last Pushed: " + str(repo.pushed_at) + "\n") 
	output += ("Star Count: " + str(repo.stargazers_count) + "\n") 
	return output

def getUserRepos(user):
	output = ""
	for repo in user.get_repos():
		output += repoToStr(repo)
	return output

def getTokenRepos(user):
	user = g.get_user()	
	output = ""
	for repo in user.get_repos():
		output += repoToStr(repo)
	return output

g = Github()

try:
	tokentext = open("token.txt")
except FileNotFoundError:
	print("Token file not found.")
	username = input("Enter GitHub username: ")
	user = g.get_user(username)	
	print(getUserRepos(user))
else:
	token = tokentext.readline()
	g = Github(token)
	print(getTokenRepos(g))
