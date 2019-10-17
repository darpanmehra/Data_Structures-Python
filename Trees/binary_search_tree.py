class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def minimum_value(self, node):
        if self.data:
            ptr = node
            while (ptr.left is not None):
                ptr = ptr.left
            return ptr

    def deletenode(self, data):
        if self.data is None:
            return self.data
        elif data < self.data:
            self.left = self.left.deletenode(data)
        elif data > self.data:
            self.right = self.right.deletenode(data)
        else:
            # case 1 where parent has no child
            if (self.right is None and self.left is None):
                del self.data
                self.data = None
                return self.data
            elif (self.left is None):  # case 2 where parent has 1 child
                current = self.data
                self.data = self.right
                del current
            elif (self.right is None):  # case 2 where parent has 1 child
                current = self.data
                self.data = self.left
                del current
            else:
                minval = self.minimum_value(self.right)
                self.data = minval.data
                self.right = self.right.deletenode(minval.data)
        return self
        # case 3 where parent has 2 children

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(str(self.data), end=' '),
        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(str(self.data), end=' ')

    def preorder(self):
        print(str(self.data), end=' ')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

if __name__ == '__main__':
    # Add Root element driver
    rootnum = int(input("Enter root element: "))
    root = Node(rootnum)

    # Insert element driver
    num_add = int(input("Enter number of elements to add: "))
    for i in range(0, num_add):
        d = int(input("Enter element: "))
        root.insert(d)

    # Print Tree driver
    printval = input("Do you wish to print tree (y/n): ")
    if printval.lower() in ['y', 'yes']:
        print("Inorder traversal: ")
        root.inorder()
        print("\n")
        print("Preorder traversal: ")
        root.preorder()
        print("\n")
        print("Postorder traversal: ")
        root.postorder()

    # Delete Node driver
    num_del_ask = input("Do you wish to delete any element (y/n): ")
    if num_del_ask.lower() in ['y', 'yes']:
        num_del = int(input("Enter element: "))
        print("Tree after deletion of element-", num_del)
        root.deletenode(num_del)
        root.inorder()