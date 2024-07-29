class WeightedGraph:
    def __init__(self) -> None:
        self.graph = dict()

    def insert(self, new_item:dict) -> None:

        if self.graph[key]:
            print('This item already exists!')
            return None

        for key, value in new_item:
            self.graph[key] = value

    def _print(self):
        print(self.graph)