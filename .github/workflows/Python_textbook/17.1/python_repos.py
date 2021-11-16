import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url,headers=headers)
print(f"Status code: {r.status_code}")
res_dict = r.json()
print(f"Total repositories: {res_dict['total_count']}")

repo_dicts = res_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

for repo in repo_dicts:
    print(f"\nName: {repo['name']}")
    print(f"Owner: {repo['owner']['login']}")
    print(f"Stars: {repo['stargazers_count']}")
    print(f"Repository: {repo['html_url']}")
    print(f"Created: {repo['created_at']}")
    print(f"Description: {repo['description']}")
