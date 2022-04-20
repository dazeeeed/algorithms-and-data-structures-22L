class AVLTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

    def get_height(self, root):
        if root is None:        # przypadek, kiedy go nie ma, bo próbujemy dostać się do dziecka liścia
            return 0     
        if root.left is None and root.right is None:
            return 1            # przypadek, kiedy jest liściem.
        else: 
            return root.height  # normalny przypadek
        
    def get_balance_factor(self, root):
        if root is None:
            return 0

        if root.right is None:
            h_right = 0
        else:
            h_right = root.right.get_height(root)

        if root.left is None:
            h_left = 0
        else:
            h_left = root.left.get_height(root)
        
        b_f = h_left - h_right
        return b_f

    def add_element(self, root, element_data):
        # if child is lesser
        if element_data < self.data:
            if self.left:
                root.left = self.left.add_element(self.left, element_data)
            else:
                root.left = AVLTreeNode(element_data)

        # is child is greater
        if element_data > self.data:
            if self.right:
                root.right = self.right.add_element(self.right, element_data) 
            else:
                root.right = AVLTreeNode(element_data)

                    
        self.height = 1 + max(self.get_height(self.left),
						self.get_height(self.right))


        balance_factor = root.get_height(root.left)-root.get_height(root.right)

        if balance_factor > 1:               # to oznacza, że lewa podgałąź jest za długa 
            balance_factor_left = root.get_height(root.left.left)-root.get_height(root.left.right)

            if balance_factor_left >= 0:
                root =  root.right_rotation(root)
            if balance_factor_left < 0:
                root.left = self.left_rotation(root.left)
                root = self.right_rotation(root)

        if balance_factor < -1:               # to oznacza, że prawa podgałąź jest za długa
            balance_factor_right = root.get_height(root.right.left)-root.get_height(root.right.right)

            if balance_factor_right <= 0:
                root =  root.left_rotation(root)
            if balance_factor_right > 0:
                root.right = self.right_rotation(root.right)
                root = self.left_rotation(root)

        return root

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

    def delete_element(self, root, element):
        if root is None:
            return root

        if element < root.data:
            root.left = self.delete_element(root.left, element)
    
        elif(element > root.data):
            root.right = self.delete_element(root.right, element)
    
        else:
            if root.left is None:
                temp = root.right           # jeśli nie ma lewego dziecka to prawe dziecko wskakuje na miejsce korzenia tego poddrzewa
                root = None                 # usunięcie korzenia
                return temp                 # zwraca nowy korzeń
    
            elif root.right is None:
                temp = root.left
                root = None
                return temp
    
            temp = self.minValueNode(root.right)                     # element ma 2 dzieci więc szukamy najmniejszego 
            root.data = temp.data                                    # następca trafia na miejsce usuniętego gościa
            root.right = self.delete_element(root.right, temp.data)  # Usunięcie tego następcy z prawej gałęzi 

        root.height = 1 + max(root.get_height(root.left),
					root.get_height(root.right))

        balance_factor = root.get_height(root.left)-root.get_height(root.right)

        if balance_factor > 1:  # to oznacza, że lewa podgałąź jest za długa 
            balance_factor_left = root.get_height(root.left.left)-root.get_height(root.left.right)

            if balance_factor_left >= 0:
                root =  root.right_rotation(root)
            if balance_factor_left < 0:
                root.left = self.left_rotation(root.left)
                root = self.right_rotation(root)

        if balance_factor < -1:  # to oznacza, że prawa podgałąź jest za długa
            balance_factor_right = root.get_height(root.right.left)-root.get_height(root.right.right)

            if balance_factor_right <= 0:
                root =  root.left_rotation(root)
            if balance_factor_right > 0:
                root.right = self.right_rotation(root.right)
                root = self.left_rotation(root)
    
        return root

    def right_rotation(self, root):
        next_root = root.left
        if next_root.right is not None:
            child = next_root.right
        else:
            child = None

        next_root.right = root      # właściwy obrót
        root.left = child           # przepisanie dziecka które pozostawiło po sobie next_root przy obrocie

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))
        next_root.height = 1 + max(self.get_height(next_root.left),
                              self.get_height(next_root.right))
        return next_root

    def left_rotation(self, root):
        next_root = root.right
        if next_root.left is not None:
            child = next_root.left
        else:
            child = None

        next_root.left = root
        root.right = child
        root.height = 1 + max(self.get_height(root.left),
                           self.get_height(root.right))
        next_root.height = 1 + max(self.get_height(next_root.left),
                           self.get_height(next_root.right))
        return next_root


    def printTree(self, level=0):
        if self != None:
            if self.right:
                self.right.printTree(level + 1)
            print(' ' * 5 * level + '-> ' + str(self.data) + "(" + str(self.get_height(self.left)-self.get_height(self.right)) + ")")

        if self.left:
            self.left.printTree(level + 1)

    @staticmethod
    def minValueNode(node):
        current = node
        while(current.left is not None):
            current = current.left
    
        return current