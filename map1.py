import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
stat = list(data["STATUS"])
elev = list(data["ELEV"])
vType = list(data["TYPE"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(zoom_start=6, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="Markers")
fg1 = folium.FeatureGroup(name="Population")


for lt, ln, st, el, vt in zip(lat, lon, stat, elev, vType):
    fg.add_child(folium.CircleMarker(location = [lt, ln],
    popup="Status: %s | Elevation: %s | Type: %s" % (st, el, vt), fill_color=color_producer(el),
    fill=True, color='#D3D3D3', fill_opacity=1))

fg1.add_child(folium.GeoJson(data=open("world.json", 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg)
map.add_child(fg1)
map.add_child(folium.LayerControl())

map.save("Map1.html")
