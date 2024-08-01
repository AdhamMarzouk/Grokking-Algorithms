class WeightedGraph:
    def __init__(self) -> None:
        # Initialize an empty dictionary to represent the graph
        self.graph = dict()

    def insert(self, new_item: dict) -> None:
        # Insert new items into the graph
        for key, value in new_item.items():
            if key in self.graph:
                # If the key already exists, update its value with the new dictionary of neighbors
                self.graph[key].update(value)
            else:
                # Otherwise, add the key with its associated dictionary of neighbors
                self.graph[key] = value

    def _print(self) -> None:
        # Print the current state of the graph
        for key, value in self.graph.items():
            print(f"{key}: {value}")

    def dijkstra(self, start_node, end_node):
        # Create a set of all nodes in the graph
        all_nodes = set(self.graph.keys())
        for key in self.graph.keys():
            all_nodes.update(self.graph[key].keys())

        # Initialize costs: set the cost to reach each node to infinity
        costs = {node: float('inf') for node in all_nodes}
        costs[start_node] = 0  # The cost to reach the start node is 0

        # Initialize parents: set the parent of each node to None
        parents = {key: None for key in all_nodes}

        # Initialize a list to keep track of processed nodes
        processed = []

        # Start with the start_node
        current_node = start_node
        
        while current_node is not None:
            cost = costs[current_node]
            neighbors = self.graph.get(current_node, {})
            for n in neighbors.keys():
                new_cost = cost + neighbors[n]
                if costs[n] > new_cost:
                    costs[n] = new_cost
                    parents[n] = current_node
            processed.append(current_node)

            # Choose the next node to process: the unprocessed node with the smallest cost
            unprocessed_nodes = {node: costs[node] for node in all_nodes if node not in processed}
            if not unprocessed_nodes:
                break
            current_node = min(unprocessed_nodes, key=unprocessed_nodes.get)
            if current_node == end_node:
                break

        # Print the costs, parents, and processed nodes (for debugging)
        print("Costs:", costs)
        print("Parents:", parents)
        print("Processed:", processed)

        # If needed, return the cost and the path to the end node
        path = []
        node = end_node
        while node is not None:
            path.append(node)
            node = parents[node]
        path.reverse()

        return costs[end_node], path
