import pandas as pd
import plotly.express as px

file = '16.2\data\japan_20190101-20211009_query.csv'

data = pd.read_csv(file)

fig = px.scatter(
    data,
    x='longitude',
    y='latitude',
    range_x=[120,150],
    range_y=[20,50],
    title='Earthquake in JP',
    size='mag',
    color='mag',
    #reversee the color scale
    color_continuous_scale=px.colors.diverging.RdYlGn[::-1],
    hover_name='place',
)

fig.show()