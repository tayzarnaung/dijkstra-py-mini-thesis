# def initial_graph() :
#     return {
                
#     # 'A': {'B':1, 'C':4, 'D':2},
#     # 'B' : {'A':9, 'E':5},
#     # 'C': {'A':4, 'F':15},
#     # 'D': {'A':10, 'F':7},
#     # 'E': {'B':3, 'J':7},
#     # 'F': {'C':11, 'D':14, 'K':3, 'G':9},
#     # 'G': {'F':12, 'I':4},
#     # 'H': {'J':13},
#     # 'I': {'G':6, 'J':7},
#     # 'J': {'H':2, 'I':4},
#     # 'K': {'F':6}
#     'A':{'B':6,'C':1},
#     'B' : {'C':4, 'E':3},
#     'C': {'D':2},
#     'D': {'E':3},
#     'E': {},

# }
    
# print(initial_graph())
# graph = initial_graph()

def dijkstra(graph,initial,x):
# initial = 'A'
# initial = input("Type source: ")
# x = input("Type destination : ")
    path = {};  adj_node = {};
    queue = []

    for node in graph:
        path[node] = float("inf")
        adj_node[node] = None
        queue.append(node)

    path[initial] = 0
    while queue:
        # find min distance which wasn't marked as current
        # print("\nQueue" + queue[0])
        key_min = queue[0]       #key_min = A
        min_val = path[key_min]  #min_val = 0
        for n in range(1, len(queue)):
            # print( path[queue[n]])
            if path[queue[n]] < min_val:            
                key_min = queue[n]  
                min_val = path[key_min]
        cur = key_min       
        queue.remove(cur)  # 'A' removed from queue. This is visited.
        # print("current: " + cur) #A
            
        for i in graph[cur]: #i=B, i=C, path[A]=0
            alternate = graph[cur][i] + path[cur]
            # print( graph[cur][i] , ' , ' , path[cur] )    
            if path[i] > alternate: #path[B]=inf, alternate =6
                # print('Path of ' , i , 'is ' , path[i])
                path[i] = alternate #6      #1
                adj_node[i] = cur   #A      #A
                # print('Path & adjacent ' ,path[i] , adj_node[i])                      
    
    # print(x, end = '<-')    
    path = []
    path.append(x)
    while True:
        x = adj_node[x]
        if x is None:
            print("")
            break
        # print(x, end='<-')
        path.append(x)
    # print("path is ", path)
    return path