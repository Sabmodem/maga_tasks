class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)

# Выводит родителя до всех его потомков
def pre_order(node, value):
    if node:
        print(node.value == 3)
        if node.value == value:
          return node

        pre_order(node.left, value)
        pre_order(node.right, value)
        
print(pre_order(tree, 3))