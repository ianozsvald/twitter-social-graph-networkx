# -*- coding: utf-8 -*-
import networkx as nx
import cPickle
import pylab
import summarise_data

MAX_FOLLWERS = 20  # limit analysis to speed up our development iterations

# load the follower networks
af = cPickle.load(open(summarise_data.ALL_NAMES))

# build a graph of all followers
G = nx.Graph()
for screen_name, followers in af.items():
    some_followers = list(followers)[:MAX_FOLLOWERS]
    G.add_node(screen_name)
    G.add_nodes_from(some_followers)
    for follower in some_followers:
        G.add_edge(follower, screen_name)

# Use graphviz
prog = "neato"  # neato is default layout engine in GraphViz
pos=nx.graphviz_layout(G, prog=prog, root=None, args="")

labels = {}
for node in G.nodes():
    labels[node] = ""
    if len(G.edges(node)) > 2:
    #if len(G.edges(node)) > 20:
        labels[node] = node

nx.draw_networkx(G, pos, with_labels=True, alpha=0.2, labels=labels, font_size=20, font_family='sans-serif')
pylab.axis("off")
pylab.title("Followers in small Twitter network")
pylab.show()
