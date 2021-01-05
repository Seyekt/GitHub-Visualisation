from github import Github
import requests
from pprint import pprint

def getUserData(username):
	url = f"https://api.github.com/users/{username}"
	userData = requests.get(url).json()
	return userData

def repoToData(user):

	repoData = {}

	repos = user.get_repos()

	for i, repo in enumerate(repos):
		repoData[i] = {'Repository Name': repo.name, 'Description': repo.description, 'Programming language': repo.language, 'Date created': repo.created_at, 
		'Date Last Pushed': repo.pushed_at, 'Repo Commits': repo.get_commits().totalCount, 'Star Count': repo.stargazers_count}

	return repoData
