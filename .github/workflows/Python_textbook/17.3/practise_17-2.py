from operator import itemgetter
from os import error
import requests
from plotly.graph_objects import bar
from plotly import offline

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Statuscode: {r.status_code}")
   
if r.status_code == 200:
    submission_ids = r.json()
    submission_dicts = []
    for submission_id in submission_ids[:30]:
        url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
        r = requests.get(url)
        if r.status_code != 200:
            print(f"Statuscode: {r.status_code}\tID:{submission_id}")
            break
        response_dict = r.json()
        try:
            submission_dict = {
                'title': response_dict['title'],
                'hn_link': f"https://hacker-news.firebaseio.com/item?id={submission_id}",
                'comments': response_dict['descendants'],
            }
        except KeyError:
            print(f"No comments exist.\tID: {submission_id}")
        else:
            submission_dicts.append(submission_dict)
    submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

    comments, links = [], []
    for i in submission_dicts:
        title = i['title']
        i_link = i['hn_link']
        link = f"<a href='{i_link}'>{title}</a>"
        comment = i['comments']

        comments.append(comment)
        links.append(link)
    
    data = [{
        'type': 'bar',
        'x': links,
        'y': comments,       
    }]

    my_layout = {
        'title': 'Most discussed articles in HackerNews',
        'xaxis':{
            'title': 'title',
            'titlefont': {'size': 24},
            'tickfont': {'size': 15}
        },
        'yaxis':{
            'title': 'comments',
            'titlefont': {'size': 24},
            'tickfont': {'size': 15}
        }
    }
    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig,filename='17.3\practise_17-2.html')
    
