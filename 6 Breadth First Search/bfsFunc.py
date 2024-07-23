class Graph:
    def __init__(self) -> None:
        # Initialize an empty graph represented as a dictionary
        self.graph = dict()

    def insert(self, new_item:dict):
        # Insert new items into the graph
        for key, value in new_item.items():
            if key in self.graph:
                # If the key already exists, extend its list with new values
                self.graph[key].extend(value)
            else:
                # Otherwise, add the key with its associated list of values
                self.graph[key] = value

    def delete(self, key:str):
        # Delete a node from the graph
        if key in self.graph:
            # Remove the key from the graph
            del self.graph[key]
            # Remove any references to this key in other nodes' adjacency lists
            for k in self.graph:
                self.graph[k] = [v for v in self.graph[k] if v != key]
        else:
            # Print a message if the key doesn't exist in the graph
            print("This key doesn't exist")

    def _print(self):
        # Print the current state of the graph
        print(self.graph)

    def bfs(self, start:str, end:str):
        # Perform Breadth-First Search (BFS) to find the shortest path from start to end
        queue = [start]  # Queue for BFS
        searched = set()  # Set to keep track of visited nodes
        parent = {start: None}  # Dictionary to store the parent of each node

        while queue:
            node = queue.pop(0)  # Dequeue the first node
            if node not in searched:
                if node == end:
                    # If the end node is found, reconstruct the path
                    shortest_path = []
                    while node is not None:
                        shortest_path.append(node)
                        node = parent[node]

                    shortest_path.reverse()  # Reverse the path to get the correct order
                    return f"Your friend {end} is here! The path to find him is: {shortest_path}"
                else:
                    searched.add(node)  # Mark the node as searched
                    for adjacent in self.graph.get(node, []):
                        if adjacent not in searched:
                            queue.append(adjacent)  # Enqueue adjacent nodes
                            parent[adjacent] = node  # Set the parent of the adjacent node

        return "Your friend is not on the list"  # Return if the end node is not found
