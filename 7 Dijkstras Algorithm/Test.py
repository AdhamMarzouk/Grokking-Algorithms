from DijkstraFunc import *

mygraph = WeightedGraph()

mygraph.insert({'start':{'a':6, 'b':2}})
mygraph.insert({'a':{'finish':1}})
mygraph.insert({'b':{'finish':5}})

mygraph._print()