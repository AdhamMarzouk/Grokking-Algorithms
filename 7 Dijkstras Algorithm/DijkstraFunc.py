class WeightedGraph:
    def __init__(self) -> None:
        self.graph = dict()

    def insert(self, new_item:dict) -> None:

        for key, value in new_item.items():
            if key in self.graph:
                self.graph[key].update(value)

            else:
                self.graph[key] = value

    def _print(self) -> None:
        for key, value in self.graph.items():
            print(f"{key}: {value}")

    def dijkstra(self, start_node, end_node):

        all_nodes = set(self.graph.keys())
        for key in self.graph.keys():
            all_nodes.update(self.graph[key].keys())

        costs = {node:float('inf') for node in all_nodes}
        costs[start_node] = 0        

        parents = {key:None for key in all_nodes}

        processed = []

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


        