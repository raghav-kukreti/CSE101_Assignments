# Dijkstra's algorithm
# First set the values of all nodes except the first and destination node to be inf
# set a as current node & make it permanent

n = int(input('Enter number of nodes: '))
graph = {}
weights = {}
for i in range(n):
	base = int(input('enter number attached to node ' +str(i) + ': '))
	temp = []
	for k in range(base):
		conn = int(input('enter connections'))
		temp.append(conn)
	graph[i] =  temp
# print(graph[0])
# find all routes to end
def find_routes(graph):
	# ideally 0 is start and n-1 is end
	con_zero = graph[0]
	con_n = graph[n-1]
	# print(con_zero, con_n)
	unvisited = []
	route = []
	for i in range(n):
		unvisited.append(i)
	# graph ->{0:[1,2], 1:[0,2,3]}
	next_node = con_zero[0]
	while(next_node != n-1):
		for i in range(len(con_zero)):
			next_node = graph[con_zero[i][i]]
			route.append(next_node)
		print(route)
		pass
find_routes(graph)
