# graph = {'a':{'b':10, 'c':3}, 'b':{'c':1, 'd':2}, 'c':{'b':4, 'd':8, 'e':2}, 'd':{'e':7}, 'e':{'d':9}}

# d = {}
# n = int(input('Enter the number of vertices: '))

# for i in range(n):
# 	d[i] = {}
# 	conn = int(input('Enter number of connections: '))
# 	for k in range(conn):
# 		con = int(input('Enter connection: '))
# 		wei = int(input('Enter weight: '))
# 		d[i][con] = wei
# print(d)

"""
Dijkstra's Algorithm in python
Relevant part above has been commented out for the test.py file to remain functional
"""
def dijkstra(graph, start, end):
	short_path = {}
	before = {}
	unvisited = graph
	inf = 9999999 
	path = []
	for node in unvisited:
		short_path[node] = inf
	short_path[start] = 0
	print(short_path)

	while unvisited:
		min_node = None
		for node in unvisited:
			if min_node is None:
				min_node = node
			elif short_path[node] < short_path[min_node]:
				min_node = node
		for childNode, weight in graph[min_node].items():
			if weight + short_path[min_node] < short_path[childNode]:
				short_path[childNode] = weight + short_path[min_node]
				before[childNode] = min_node
		unvisited.pop(min_node)

	currentNode = end

	while currentNode != start:
		try:
			path.insert(0, currentNode)
			currentNode = before[currentNode]
		except KeyError:
			print("Path not reachable")
			break

	path.insert(0, start)
	
	if short_path[end] != inf:
		# print('Shortest path: ' + str(short_path[end]))
		# print('And path is : ' + str(path))
		return path

# dijkstra(d, 0 , 3)