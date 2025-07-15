def check_mirror(n, tree1_edges, tree2_edges):
    # Arrays to store left and right children for both trees
    left1 = [-1] * (n + 1)
    right1 = [-1] * (n + 1)
    left2 = [-1] * (n + 1)
    right2 = [-1] * (n + 1)

    # Build Tree 1
    for edge in tree1_edges:
        u, v, d = edge
        if d == 'L':
            left1[int(u)] = int(v)
        else:
            right1[int(u)] = int(v)

    # Build Tree 2
    for edge in tree2_edges:
        u, v, d = edge
        if d == 'L':
            left2[int(u)] = int(v)
        else:
            right2[int(u)] = int(v)

    # Compare left of Tree1 with right of Tree2 and vice versa
    for i in range(1, n + 1):
        if left1[i] != right2[i] or right1[i] != left2[i]:
            return "no"
    
    return "yes"


# Input handling: Ensure input is as expected
try:
    # Number of nodes
    n = int(input("Enter number of nodes: "))
    if n <= 1:
        raise ValueError("The number of nodes must be greater than 1.")

    # Read edges for both trees
    print(f"Enter {n-1} edges for Tree 1:")
    tree1_edges = [input().split() for _ in range(n - 1)]
    
    print(f"Enter {n-1} edges for Tree 2:")
    tree2_edges = [input().split() for _ in range(n - 1)]

    # Output the result of check_mirror function
    print(check_mirror(n, tree1_edges, tree2_edges))

except ValueError as e:
    print(f"Error: {e}")
