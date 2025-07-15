from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def build_tree(n, edges):
    nodes = [None] * (n + 1)
    has_parent = [False] * (n + 1)

    for u, v, c in edges:
        u = int(u)
        v = int(v)
        if nodes[u] is None:
            nodes[u] = Node(u)
        if nodes[v] is None:
            nodes[v] = Node(v)

        if c == 'L':
            nodes[u].left = nodes[v]
        else:
            nodes[u].right = nodes[v]
        has_parent[v] = True

    # Find the root (node that doesn't have a parent)
    for i in range(1, n + 1):
        if not has_parent[i]:
            return nodes[i]
    return None

def zigzag_traversal(root):
    if not root:
        return

    result = []
    q = deque()
    q.append(root)
    left_to_right = True

    while q:
        level_size = len(q)
        level = [0] * level_size

        for i in range(level_size):
            node = q.popleft()

            # insert based on direction
            index = i if left_to_right else (level_size - 1 - i)
            level[index] = node.data

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        result.extend(level)
        left_to_right = not left_to_right

    print(' '.join(map(str, result)))

# Read input
n = int(input())
edges = [input().split() for _ in range(n - 1)]

# Build tree and perform zigzag traversal
root = build_tree(n, edges)
zigzag_traversal(root)