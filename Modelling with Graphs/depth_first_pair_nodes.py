import networkx as nx
import graph6
import graph7
import graph8
import graph9
import graph10


def dfs(G,a,b,u):

    # set distance of a to 0
    G.node[a]["label"] = 0

    # mark that node as visited and print it out
    G.node[u]["visited"] = "yes"
    print(u)

    # if the current node is the node that you're looking for, set rest of nodes to visited
    # this prevents the dfs from continuing
    # it's dirty but it works
    if u == b:
        nx.set_node_attributes(G, "yes", "visited")
    else:
        for v in sorted(G.neighbors(u)):  # just in case, making sure nodes are sorted to definitely pick the smallest
            if G.node[v]["visited"] == "no":
                # distance = distance of predecessor + 1
                G.node[v]["label"] = G.node[u]["label"] + 1
                dfs(G, a, b, v)


print()
G6=graph6.Graph()
a=12
b=40
print('Depth-First-Search visited the following nodes of G6 in this order:')
dfs(G6,a,b,a)  ### count the DFS-path from a to b, starting at a
print('Depth-First Search found a path in G6 between vertices', a, 'and', b, 'of length', G6.node[b]['label'])
print()


G7=graph7.Graph()
a=5
b=36
print('Depth-First-Search visited the following nodes of G7 in this order:')
dfs(G7,a,b,a)  ### count the DFS-path from a to b, starting at a
print('Depth-First Search found a path in G7 between vertices', a, 'and', b, 'of length', G7.node[b]['label'])
print()


G8=graph8.Graph()
a=15
b=40
print('Depth-First-Search visited the following nodes of G8 in this order:')
dfs(G8,a,b,a)  ### count the DFS-path from a to b, starting at a
print('Depth-First Search found a path in G8 between vertices', a, 'and', b, 'of length', G8.node[b]['label'])
print()


G9=graph9.Graph()
a=1
b=19
print('Depth-First-Search visited the following nodes of G9 in this order:')
dfs(G9,a,b,a)  ### count the DFS-path from a to b, starting at a
print('Depth-First Search found a path in G9 between vertices', a, 'and', b, 'of length', G9.node[b]['label'])
print()


G10=graph10.Graph()
a=6
b=30
print('Depth-First-Search visited the following nodes of G10 in this order:')
dfs(G10,a,b,a)  ### count the DFS-path from a to b, starting at a
print('Depth-First Search found a path in G10 between vertices', a, 'and', b, 'of length', G10.node[b]['label'])
print()
