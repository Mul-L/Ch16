from operator import itemgetter
from os import error
import requests

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

    for s in submission_dicts:
        print(f"\nTitle: {s['title']}")
        print(f"Discussion link: {s['hn_link']}")
        print(f"Comments: {s['comments']}")