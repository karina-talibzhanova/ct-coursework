import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5


def find_next_vertex(G, i):

	# have a node, find its neighbours, visit the neighbour with the smallest label
	# but i'm not given a node to examine in this function..... although i could modify it
	# need to mark which nodes have been visited <-- this requires an attribute alongside color

	for j in nx.neighbors(G, i):
		if G.node[j]["visited"] == "no":
			G.node[j]["visited"] = "yes"
			return j


def find_smallest_color(G, i):

	current = 1
	color_set = set()

	for j in nx.neighbors(G, i):
		color_set.add(G.node[j]["color"])

	while True:
		if current not in color_set:
			break
		else:
			current += 1

	G.node[i]["color"] = current






def greedy(G):
	global kmax
	global visited_counter

	nx.set_node_attributes(G, 0, "color")

	next = 1

	while "no" in G.nodes.data("visited").values():
		find_smallest_color(G, next)
		next = find_next_vertex(G, next)









	print()
	for i in G.nodes():
		print('vertex', i, ': color', G.node[i]['color'])
	print()
	print('The number of colors that Greedy computed is:', kmax)
	print()



print('Graph G1:')
G=graph1.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G2:')
G=graph2.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G3:')
G=graph3.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G4:')
G=graph4.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G5:')
G=graph5.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)