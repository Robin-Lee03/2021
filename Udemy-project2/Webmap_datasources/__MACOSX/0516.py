import folium
import pandas

# map = folium.Map(location=[48.23,16.45])
# map.save("Map1.html")
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])


map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for ln, lt in zip(lon, lat):
    fg.add_child(folium.Marker(location=[ln,lt], popup="I'm a marker", icon=folium.Icon(color='green')))


map.add_child(fg)

map.save("Map.html")