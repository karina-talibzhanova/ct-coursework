import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5


# original function didn't have param i
# there should be a way to do it with just the one parameter
def find_next_vertex(G, next):
	global vertices

	for i in nx.neighbors(G, next):
		if G.node[i]["visited"] == "no":
			vertices.add(i)

	vertices.remove(next)

	if len(vertices) == 0:
		return -1

	return min(vertices)


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
	global vertices

	nx.set_node_attributes(G, 0, "color")

	vertices = {1}

	next = 1

	# colour the graph while some nodes remain unvisited
	while "no" in nx.get_node_attributes(G, "visited").values():
		find_smallest_color(G, next)
		G.node[next]["visited"] = "yes"
		next = find_next_vertex(G, next)

	color_vals = list(nx.get_node_attributes(G, "color").values())
	kmax = max(color_vals)

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