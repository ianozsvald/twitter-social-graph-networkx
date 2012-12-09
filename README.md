twitter-social-graph-networkx
=============================

Download, summarise and visualise the followers in a small twitter social network using NetworkX

Uses
----

* https://github.com/ianozsvald/python-twitter  # forked from bear
* NetworkX
* numpy 1.6.2 (for NetworkX)
* matplotlib (for NetworkX)
* graphviz (and -dev for NetworkX) with pygraphviz

Setup
-----

    $ pip install -r requirements.txt

Usage
-----

    $ python get_data.py  # download friend+follower data to ./data
    $ python summarise_data.py  # generate ./data/all_names.pickle by extracting followers
    $ python draw_network.py  # draw a network using GraphViz in NetworkX
