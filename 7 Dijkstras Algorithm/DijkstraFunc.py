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

    def dijkstra():
        visited = set()
        