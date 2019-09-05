import pandas as pd

df = pd.read_csv('haversine/distance_csv/distance.csv')
conn = {}

# for name,lat, lon, in zip(df.Name,df.Latitude,df.Longitude):
#     sub_row= {}
#     sub_row.append(name)
#     for lat2, lon2, in zip(df.Latitude,df.Longitude):
#         distance = haversine(lat,lon,lat2,lon2)
#         sub_row.append( distance)
#     row.append(sub_row)

graph = {
    'a':{'b':3,'c':1},
    'b' : {'a':3,'c':7, 'd':5, 'e':1},
    'c': {'a':1, 'b':7, 'd':2},
    'd': {'b':5, 'c':2, 'e':7},
    'e': {'b':1, 'd':7}
}

graph_d = {
		'Sule':{'Sule Myodaw Hall':0.2779, 'Pan Soe Tan':0.3089},
		'Sule Myodaw Hall':{'Bar Lan':2}	
}

test = {
	'a':{'b':0.2779,'aa':0.3089},
	'b':{'c':0.2671, 'bb':0.3192},
	'c':{'d':0.4453,'cc':0.3196},
	'd':{'e':0.4012}
	}

# arr =[]
# for i in range(10):
#     # print (i)
#     arr.append(i)
# print ('arr' , arr)