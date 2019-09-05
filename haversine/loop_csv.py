import pandas as pd
import csv
import math

dictionary= {}; distance = []; header=['a','b','c']
# header = ['Sule', 'Sule Myodaw Hall', 'Yoke Shin Yone']

with open('distance_csv/dist.csv', 'r') as readFile:
	reader = csv.reader(readFile)	
	
	for row in reader:
		sub_dist = []
		for column in row:
			# if column == '0': continue;	
			if column == '':	continue;		
			sub_dist.append(column)
		distance.append(sub_dist)
	distance = list(filter(None, distance)) #remove empty index from string list
	print(distance)
readFile.close()
# print(header[1])
# print(distance[1][0])

# for h in header:
# 	for d in distance:
# 		if h== d: continue
# 		dictionary.update({'key3':'geeks'}) 
		# dictionary.update(newkey1 ='portal') 

# print(len(point), point)  #length = 3 .i.e index 0,1,2
# print (df.point[0])
# for n in range(1,len(point)): #1,2

for n in range(len(header)): #0,1,2	 #row
	sub_dict ={}
	prefix = header[n];	dist = distance[n]
	dist.pop(0) #remove an element from a list by index
	# print('d',dist)

	# sub_dict.update({'a':0,'b':1})
	# dictionary.update({'a':sub_dict})  #{'a': {'a': 0, 'b': 1}}

	for i in range(len(header)):	#0,1,2	#column
		sub_dict.update({header[i]:dist[i]})
	# print('s_d',sub_dict)
	dictionary.update({prefix:sub_dict})
print('final',dictionary)

