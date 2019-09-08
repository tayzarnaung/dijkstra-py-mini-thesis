def fun( x, y, weight):
	print(x, y, weight)

fun('a',b,3)
arr = []
# ('X', 'A', 7),
for i in range(3):
	x = 'A'
	y = 'B'
	dist = input("Type distance: ")

	string = x +', '+ y +', '+ dist 
	print (string)
	arr.append(string)
print(arr)

# for edge in edges:
#     graph.add_edge(*edge)

for i in arr:
	print(*i)