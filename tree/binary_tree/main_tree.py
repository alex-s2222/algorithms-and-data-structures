class Node:
    def __init__(self, data):
        self.left = None
        self.right = None 
        self.data = data

    # insert 
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


    # print Tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()
   
   # left-root-right
    def inorder_travel(self, root):
        res = []
        if root:
            res = self.inorder_travel(root.left)
            res.append(root.data)
            res = res + self.inorder_travel(root.right)
        return res
    
    # left-root-right
    def preorder_travel(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorder_travel(root.left)
            res = res + self.preorder_travel(root.right)
        return res
    
    # left - rigth - root 
    def postorder_travel(self, root):
        res =[]
        if root:
            res = self.postorder_travel(root.left)
            res = res + self.postorder_travel(root.right)
            res.append(root.data)
        return res




def create_tree() -> Node:
    arr = [10, 6 ,5 , 3, 7, 9, 8, 15, 12, 11, 13, 20, 19, 21]
    fl = 0 
    
    for i in arr:
        if fl:
            root.insert(i)
        else:
            root = Node(i)
            fl = 1

    return root


root = create_tree()

root.print_tree()
print(root.inorder_travel(root))
print(root.preorder_travel(root))
print(root.postorder_travel(root))


