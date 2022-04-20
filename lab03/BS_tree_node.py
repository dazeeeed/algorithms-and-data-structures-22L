class BSTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, child_data):
        # if child is lesser
        if child_data < self.data:
            if self.left:
                self.left.add_child(child_data)
            else:
                self.left = BSTreeNode(child_data)

        # is child is greater
        if child_data > self.data:
            if self.right:
                self.right.add_child(child_data) 
            else:
                self.right = BSTreeNode(child_data)

    def get_traversal(self):
        elements = []

        # left tree
        if self.left:
            elements += self.left.get_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.get_traversal()

        return elements

    def search_element(self, element):
        if self.data == element:
            return True

        if element < self.data:
            if self.left:
                return self.left.search_element(element)
            else:
                return False

        if element > self.data:
            if self.right:
                return self.right.search_element(element)
            else:
                return False

    def printTree(self, level=0):
        if self != None:
            if self.right:
                self.right.printTree(level + 1)

            print(' ' * 4 * level + '-> ' + str(self.data))

        if self.left:
            self.left.printTree(level + 1)


    def delete_element(self, root, element):
        if root is None:
            return root

        if element < root.data:
            root.left = self.delete_element(root.left, element)
    
        elif(element > root.data):
            root.right = self.delete_element(root.right, element)
    
        else:
            if root.left is None:
                temp = root.right # jeśli nie ma lewego dziecka to prawe dziecko wskakuje na miejsce korzenia tego poddrzewa
                root = None       # usunięcie korzenia
                return temp       # zwraca nowy korzeń
    
            elif root.right is None:
                temp = root.left
                root = None
                return temp
    
            # if this element has 2 children then it will be replaced by its smaller descendant
            temp = self.minValueNode(root.right)

            root.data = temp.data
    
            # Delete the inorder successor
            root.right = self.delete_element(root.right, temp.data)
    
        return root

    @staticmethod
    def minValueNode(node):
        current = node
    
        # loop down to find the leftmost leaf
        while(current.left is not None):
            current = current.left
    
        return current
            