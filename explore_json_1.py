import json
import plotly

infile = open("eq_data_1_day_m1.json", "r")
outfile = open("readable_eq_data.json", "w")

eq_data = json.load(infile)

json.dump(eq_data, outfile, indent=4)

list_of_eqs = eq_data["features"]
mags, lons, lats = [], [], []
for i in list_of_eqs:
    mag = i["properties"]["mag"]
    lon = i["geometry"]["coordinates"][0]
    lat = i["geometry"]["coordinates"][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
print(mags[:10])
print(lons[:10])
print(lats[:10])
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [Scattergeo(lon=lons, lat=lats)]
my_layout = Layout(title="Global Earthquakes")
fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="global_earthquakes.html")
