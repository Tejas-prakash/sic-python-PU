class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def build_tree(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while i < len(nodes):
        current = queue.pop(0)
        if i < len(nodes):
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
            i += 1
        if i < len(nodes):
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
            i += 1
    return root

def height(root):
    if root is None:
        return 0  # Return 0 for an empty tree
    left_height = height(root.left)
    right_height = height(root.right)
    return 1 + max(left_height, right_height)

# Input handling
n = int(input("Enter number of nodes: "))  # number of nodes
nodes = list(map(int, input("Enter the node values: ").split()))

# Build the tree
root = build_tree(nodes)

# Output the height of the tree
print("Height of the tree:", height(root))
