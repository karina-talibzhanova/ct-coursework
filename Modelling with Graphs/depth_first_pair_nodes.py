import networkx as nx
import graph6
import graph7
import graph8
import graph9
import graph10

# count the length of the path between two pre-specified vertices a and b, using Depth-First-Search
#
# def dfs(G,u):
#     n = len(G.nodes())
#     global visited_counter
#     G.node[u]['visited'] = 'yes'
#     visited_counter = visited_counter + 1
#     print(u)
#     if visited_counter < n:
#         for v in G.neighbors(u):
#             if G.node[v]['visited'] == 'no':
#                 dfs(G,v)

# G is the graph, a,b are given nodes of G, u is the start node
# u is also where you currently are because recursion is a thing

def dfs(G,a,b,u):
    n = len(G.nodes())

    # does not calculate distances yet
    # also does not stop until it finds b
    # it's all this weird recursion and stuff
    # when it finds b, it goes back up the stack and will continue to recurse and find the next unvisited neighbor
    G.node[u]["visited"] = "yes"
    print(u)
    print(G.node[u]["visited"])
    print(G.node[u]["label"])

    if u == b:
        return "found"
    for v in G.neighbors(u):
        if G.node[u]["visited"] == "no":
            dfs(G, a, b, v)

    # if u != b:
    #     for v in G.neighbors(u):
    #         if G.node[v]["visited"] == "no":
    #             dfs(G, a, b, v)


G6 = graph6.Graph()
a = 12
b = 40
dfs(G6, a, b, a)




# print()
# G6=graph6.Graph()
# a=12
# b=40
# print('Depth-First-Search visited the following nodes of G6 in this order:')
# dfs(G6,a,b,a)  ### count the DFS-path from a to b, starting at a
# print('Depth-First Search found a path in G6 between vertices', a, 'and', b, 'of length', G6.node[b]['label'])
# print()
#
#
# G7=graph7.Graph()
# a=5
# b=36
# print('Depth-First-Search visited the following nodes of G7 in this order:')
# dfs(G7,a,b,a)  ### count the DFS-path from a to b, starting at a
# print('Depth-First Search found a path in G7 between vertices', a, 'and', b, 'of length', G7.node[b]['label'])
# print()
#
#
# G8=graph8.Graph()
# a=15
# b=40
# print('Depth-First-Search visited the following nodes of G8 in this order:')
# dfs(G8,a,b,a)  ### count the DFS-path from a to b, starting at a
# print('Depth-First Search found a path in G8 between vertices', a, 'and', b, 'of length', G8.node[b]['label'])
# print()
#
#
# G9=graph9.Graph()
# a=1
# b=19
# print('Depth-First-Search visited the following nodes of G9 in this order:')
# dfs(G9,a,b,a)  ### count the DFS-path from a to b, starting at a
# print('Depth-First Search found a path in G9 between vertices', a, 'and', b, 'of length', G9.node[b]['label'])
# print()
#
#
# G10=graph10.Graph()
# a=6
# b=30
# print('Depth-First-Search visited the following nodes of G10 in this order:')
# dfs(G10,a,b,a)  ### count the DFS-path from a to b, starting at a
# print('Depth-First Search found a path in G10 between vertices', a, 'and', b, 'of length', G10.node[b]['label'])
# print()
