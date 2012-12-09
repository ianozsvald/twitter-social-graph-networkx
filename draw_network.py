# -*- coding: utf-8 -*-
import networkx as nx
import cPickle
import pylab
import summarise_data

MAX_FOLLOWERS = 99900  # limit analysis to speed up our development iterations

# load the follower networks
af = cPickle.load(open(summarise_data.ALL_NAMES))

# build a graph of all followers
Gf = nx.Graph()
for screen_name, followers in af.items():
    some_followers = list(followers)[:MAX_FOLLOWERS]
    Gf.add_node(screen_name)
    Gf.add_nodes_from(some_followers)
    for follower in some_followers:
        Gf.add_edge(follower, screen_name)

# shave off followers who are follow nobody in our inner network, so NetworkX
# can plot a sane number of people at the edge of the graph
MAX_WITH_0_FOLLOWERS = 40
for screen_name, followers in af.items():
    nbr_with_no_followers = 0
    for follower in followers:
        edges_of_connected_node = Gf.edges(follower)
        if len(edges_of_connected_node) == 1:
            if nbr_with_no_followers == MAX_WITH_0_FOLLOWERS:
                Gf.remove_node(follower)
            else:
                nbr_with_no_followers += 1
    print "Capping:", screen_name, nbr_with_no_followers


# Use graphviz
prog = "neato"  # neato is default layout engine in GraphViz
pos = nx.graphviz_layout(Gf, prog=prog, root=None, args="")

labels = {}
for node in Gf.nodes():
    labels[node] = ""
    if len(Gf.edges(node)) > 10:
        labels[node] = node

nx.draw_networkx(Gf, pos, with_labels=True, alpha=0.2, labels=labels, font_size=20, font_family='sans-serif')
pylab.axis("off")
pylab.title("Followers in small Twitter network")
pylab.show()
