import folium
import pandas as pd
import dijkstra_sp as dijk
import sp as sPath
import graph_distance as graph_distance


m = folium.Map(location=[16.7982,96.1422],zoom_start=14)

test_cor= pd.read_csv('test_cor.csv')
## print( test_cor.get('Name') )

bus_stop = pd.read_csv('sule_shwedagon.csv')
# bus_stop = pd.read_csv('bus_stop.csv')

incidents = folium.map.FeatureGroup()

for lat, lng, in zip(test_cor.Latitude,test_cor.Longitude):
    incidents.add_child(
        folium.CircleMarker(
            [lat, lng],
            radius=5, # define how big you want the circle markers to be
            color='red',
            fill=True,
            fill_color='green',
            fill_opacity=0.6
        )
    )


for name,lat, lng, in zip(bus_stop.Name,bus_stop.Latitude,bus_stop.Longitude):
    marker3 = folium.Marker(location=[lat, lng], popup=name).add_to(m)
    # incidents.add_child(
    #     folium.CircleMarker(
    #         [lat, lng],
    #         radius=5, 
    #         color='red',
    #         fill=True,
    #         fill_color='blue',
    #         fill_opacity=0.6
    #     )
    # )    

m.add_child(incidents)


# dijk.dijkstra(graph, 'a', 'e')
start = input("Type a new source: ")
end = input("Type a new destination : ")
sPath = sPath.dijkstra(graph_distance.graph, start, end)
path = dijk.dijkstra(graph_distance.graph, start, end)
print("sp" , sPath)
print("dijk" , path)

toDraw= []; poly =[];

for p in path:
    for name,lat,lng in zip(test_cor.Name,test_cor.Latitude,test_cor.Longitude):            
        if p == name:
            # print (name, lat , lng); # break;
            # toDraw.append(lat); toDraw.append(lng);            
        # else: print(p)
            # poly.append( [lat , lng] )
            # print("line will connect " , name)
            toDraw.append( { 'name': name,'lat': lat,"lng": lng } ) 



for name,lat,lng in zip(bus_stop.Name,bus_stop.Latitude,bus_stop.Longitude):    
    poly.append( [lat , lng] )

            

# print ("Polyline" , poly)

# print(toDraw); print (toDraw[0]['lat'])
# for i in toDraw:
#     print (i['lat'])

# folium.PolyLine(poly, color="blue", weight=2.5, opacity=1).add_to(m)
m.save("index1.html")