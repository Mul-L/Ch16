from plotly.graph_objects import bar
from plotly import offline
import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Statuscode: {r.status_code}")

response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []
for repo in repo_dicts:
    repo_url = repo['html_url']
    repo_name = repo['name']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>" # 将x轴标签设置为超链接
    repo_links.append(repo_link)
    stars.append(repo['stargazers_count'])

    owner = repo['owner']['login']
    description = repo['description']    
    label = f"{owner}<br />{description}" # Ploty中允许使用HTML元素【注意空格】
    labels.append(label)

data = [{
    'type': 'bar',
    'x': repo_links, 
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60,100,150)',
        'line': {'width': 1.5, 'color': 'rgb(25,25,25)'}
    },
    'opacity': 0.6,
}]
my_layout = {
    'title':'The most popular Python respositories in Github',
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data':data, 'layout':my_layout}
offline.plot(fig,filename='17.1\python_repos.html')