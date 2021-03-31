class Node:
    def __init__(self, item):
        self.children = []
        self.item = item

    def add_child(self, item):
        self.children.append(Node, item)

    # Time O(V + E) | Space O(V)
    def depth_first_search(self, array):
        array.append(self.item)
        for child in self.children:
            children.depth_first_search(array)
        return array