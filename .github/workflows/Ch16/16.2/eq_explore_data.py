import json
import plotly.express as px

filename = '16.2\data\eq_data_1_day_m1.json'
with open(filename) as f:
    all_data = json.load(f)

readable_file = '16.2/data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_data, f, indent=4)

all_eq_dicts = all_data['features']

mags, titles, lons, lats = [], [], [], []
for eq_dic in all_eq_dicts:
    mag = eq_dic['properties']['mag']
    title = eq_dic['properties']['title']
    lon = eq_dic['geometry']['coordinates'][0]
    lat = eq_dic['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

fig = px.scatter(
    x=lons,
    y=lats,
    labels={'x':'longitude', 'y':'latitude'},
    range_x=[-200,200],
    range_y=[-90,90],
    width=800,
    height=800,
    title='Global Earthquake Scatter Chart',
)

fig.write_html('16.2/data/global_eq.html')
fig.show()