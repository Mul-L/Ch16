import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url,headers=headers)
print(f"Status code: {r.status_code}")
res_dict = r.json()
print(f"Total repositories: {res_dict['total_count']}")

repo_dicts = res_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

repo_dict = repo_dicts[0]
print(f"\nKey: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)