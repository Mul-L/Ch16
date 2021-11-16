import requests
import json

url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Statuscode: {r.status_code}")

if r.status_code == '200':
    response_dict = r.json()
    readable_file = '17.3/data/readable_hn_article_data.json'
    with open(readable_file,'w')as f:
        json.dump(response_dict, f, indent=4)