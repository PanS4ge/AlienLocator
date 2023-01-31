import folium
import json
import requests
from folium.plugins import MarkerCluster

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'

req = requests.get('https://data.nasa.gov/resource/gh4g-9sfh.json')
js = req.json()

world_map = folium.Map(tiles="cartodbpositron")
marker_cluster = MarkerCluster().add_to(world_map)

for x in js:
    try:
        lat = x['geolocation']['latitude']
        long = x['geolocation']['longitude']
        radius=5
        col = ''
        if(x['recclass'] == "Unknown"):
            col = bcolors.FAIL
            popup_text = f"""{x['name']}<br>
                            ID: {x['id']}<br>
                            Class: {x['recclass']}<br>
                            Year: {x['year'].split("T")[0]}
            """
        else:
            try:
                col = bcolors.OKGREEN
                popup_text = f"""{x['name']}<br>
                                ID: {x['id']}<br>
                                Class: {x['recclass']}<br>
                                Mass: {x['mass']}<br>
                                Year: {x['year']}
                """
            except:
                col = bcolors.WARNING
                popup_text = f"""{x['name']}<br>
                            ID: {x['id']}
                """
    except Exception as e:
        popup_text = f"""{x['name']}<br>
                    BLAD ZDOBYCIA<br>
                    {str(e)}
        """
        pass
    #print(x['name'])
    folium.CircleMarker(location = [lat, long], radius=radius, popup= popup_text, fill =True).add_to(marker_cluster)

#for i in range(len(df)):
#        lat = df.iloc[i]['Latitude']
#        long = df.iloc[i]['Longitude']
#        radius=5
#        popup_text = """Country : {}<br>
#                    %of Users : {}<br>"""
#        popup_text = popup_text.format(df.iloc[i]['Country'],
#                                   df.iloc[i]['User_Percent']
#                                   )
#        folium.CircleMarker(location = [lat, long], radius=radius, popup= popup_text, fill =True).add_to(marker_cluster

world_map.save('alien.html')
