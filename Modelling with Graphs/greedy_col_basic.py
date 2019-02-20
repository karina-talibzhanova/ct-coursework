import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5


def find_smallest_color(G, i):
	n = len(G.nodes())  # number of nodes in G
	# get given a graph G with a bunch of nodes, and a particular node
	# check the nodes i is connected to and their colour values
	# take next highest colour value <-- wrong. take lowest possible colour value
	# this may require a while loop
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

	nx.set_node_attributes(G, 0, "color")

	for n in G.nodes():
		find_smallest_color(G, n)

	color_vals = list(nx.get_node_attributes(G, "color").values())
	kmax = max(color_vals)

	print()
	for i in G.nodes():
		print('vertex', i, ': color', G.node[i]['color'])
	print()
	print('The number of colors that Greedy computed is:', kmax)



print('Graph G1:')
G = graph1.Graph()
greedy(G)

print('Graph G2:')
G = graph2.Graph()
greedy(G)

print('Graph G3:')
G = graph3.Graph()
greedy(G)

print('Graph G4:')
G = graph4.Graph()
greedy(G)

print('Graph G5:')
G = graph5.Graph()
greedy(G)
