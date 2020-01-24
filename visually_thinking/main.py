import plotly.graph_objects as go
import plotly.express as px
import pandas
import json

data = pandas.read_csv(r"C:\Users\davis\Documents\GitHub\Plotly-Plots\visually_thinking\data\cats_per_district.csv")
with open(r'C:\Users\davis\Documents\GitHub\Plotly-Plots\visually_thinking\data\all.geojson') as r:
    geojson = json.load(r)

# fig = px.choropleth_mapbox(data, geojson=geojson)
fig = go.Figure(go.Choroplethmapbox(geojson=geojson, locations=data.PostcodeDistrict, z=data.EstimatedCatPopulation,
                                    colorscale="Viridis", zmin=0, zmax=12,
                                    marker_opacity=0.5, marker_line_width=0))

fig.update_layout(mapbox_style="carto-positron",
                  mapbox_zoom=3, mapbox_center = {"lat": 37.0902, "lon": -95.7129})
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
