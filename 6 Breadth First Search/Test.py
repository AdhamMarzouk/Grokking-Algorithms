from bfsFunc import Graph  # Import the Graph class from the bfsFunc module

# Create an instance of the Graph class
mygraph = Graph()

# Insert nodes and their connections into the graph
mygraph.insert({'friend_a': ['friend_b', 'friend_c', 'friend_d']})
mygraph.insert({'friend_b': ['friend_e', 'friend_f', 'friend_g']})
mygraph.insert({'friend_c': ['friend_f', 'friend_h', 'friend_i', 'friend_j']})

# Perform Breadth-First Search (BFS) to find the shortest path from 'friend_a' to 'friend_j'
print(mygraph.bfs('friend_a', 'friend_j'))   #output: Your friend friend_j is here! The path to find him is: ['friend_a', 'friend_c', 'friend_j']
