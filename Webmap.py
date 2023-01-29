import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = data['LAT']
lon = data['LON']
elev = data['ELEV']
name = data['NAME']


def color_codes(codes):
    if codes < 1500:
        return 'green'
    elif 1500< codes < 3000:
        return 'orange'
    else:
        return 'red'


WEB = folium.Map([42.82430058704484, -112.4470987350125], zoom_start=5, tiles='openstreetmap')
fgv = folium.FeatureGroup(name="Volcanoes")
for LT, LN, EL,NM in zip(lat, lon, elev, name):
    fgv.add_child(folium.CircleMarker(location=(LT, LN), radius=6, popup=NM + '\n'+ str(EL) +'m',
                            tooltip="for more information. Click here", fill_color=color_codes(EL),
                            fill=True, fill_opacity=0.7, color='black'))

fgp = folium.FeatureGroup(name='Population')
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                             style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005']<10000000
                             else 'orange' if 10000000 <= x['properties']['POP2005'] < 100000000 else 'red'}))
WEB.add_child(fgv)
WEB.add_child(fgp)
WEB.add_child(folium.LayerControl())
WEB.save("webmap1.html")
