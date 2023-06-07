import os
from github import Github

github = Github(os.getenv('GITHUB_TOKEN'))

repositories = github.search_repositories(query='language:python archived:NOT is:public stars:>10000 forks:>500')
for repo in repositories.get_page(2):
    print(repo.name, repo.html_url)
