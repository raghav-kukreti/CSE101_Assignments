"""
Breadth First Search algorithm in Python
"""
def create_nodes(number_of_nodes):
	return [i for i in range(1, number_of_nodes+1)]

def make_link(G, node1, node2):
	if node1 not in G:
		G[node1]={}
	G[node1][node2]=1
	if node2 not in G:
		G[node2]={}
	G[node2][node1]=1

def find_all_distance(G, s_node):
    open_list=[s_node]
    distances_from_start={}
    distances_from_start[s_node]=0
    while open_list:
        cur_node = open_list.pop(0)
        if cur_node not in G:
            continue
        for neighbour in G[cur_node]:
            if neighbour not in distances_from_start:
                distances_from_start[neighbour] = distances_from_start[cur_node] + 6
                open_list.append(neighbour)
    return distances_from_start

no_vertices = int(input())

for i in range(no_vertices):
    [no_nodes, no_edges] = input().split()
    nodes = create_nodes(int(no_nodes))
    G={}
    for j in range(int(no_edges)):
        [node1, node2] = input().split()
        make_link(G, int(node1), int(node2))
    s_node = int(input())
    distance_from_start = find_all_distance(G, s_node)
    for node in nodes:
        if node == s_node: continue
        if node in distance_from_start:
            print(distance_from_start[node], end=" ")
        else:
            print(-1, end=" ")    
    print('')
  
