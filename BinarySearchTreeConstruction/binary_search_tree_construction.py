class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Average: Time O(log(N)) | Space O(1) || Worst: Time O(N) | Space O(1)
    def insert(self, value):
        current_note = self
        while True:
            if value < current_note.value:
                if current_note.left is None:
                    current_note.left = BST(value)
                    break
                else:
                    current_note = current_note.left
            else:
                if current_note.right is None:
                    current_note.right = BST(value)
                    break
                else:
                    current_note = current_note.right
        return self

    # Average: Time O(log(N)) | Space O(1) || Worst: Time O(N) | Space O(1)
    def contain(self, value):
        current_note = self
        while current_note is not None:
            if value < current_note.value:
                current_note = current_note.left
            elif value > current_note.value:
                current_note = current_note.right
            else:
                return True
        

    def remove(self, value, parent_node = None):
        current_note = self
        while current_note is not None:
            if value < current_note.value:
                parent_node = current_note
                current_note = current_note.left
            elif value > current_note.value:
                parent_node = current_note
                current_note = current_note.right
            else:
                if current_note.left is not None and current_note.right is not None:
                    # current_node.value is smallest value of right subtree
                    current_note.value = current_note.right.get_min_value()
                    current_note.right.remove(current_note.value, current_note)
            