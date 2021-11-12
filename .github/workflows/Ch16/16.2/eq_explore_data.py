import json
import plotly.express as px
import pandas as pd

filename = '16.2\data\eq_data_30_day_m1.json'
with open(filename) as f:
    all_data = json.load(f)

# readable_file = '16.2\data\readable_eq_data.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_data, f, indent=4)

fig_title = all_data['metadata']['title']
all_eq_dicts = all_data['features']
mags, titles, lons, lats = [], [], [], []

for eq_dic in all_eq_dicts:
    mags.append(eq_dic['properties']['mag'])
    titles.append(eq_dic['properties']['title'])
    lons.append(eq_dic['geometry']['coordinates'][0])
    lats.append(eq_dic['geometry']['coordinates'][1])

data = pd.DataFrame(
    data=zip(lons, lats, titles, mags), columns=['longitude', 'latitude', 'location', 'mags']
)
data.head()

fig = px.scatter(
    data,
    x='longitude',
    y='latitude',
    range_x=[-200,200],
    range_y=[-90,90],
    width=800,
    height=800,
    title=fig_title,
    size='mags',
    size_max=10,
    color='mags',
    #color_continuous_scale=px.colors.qualitative.Antique,
    hover_name='location',
)

fig.show()