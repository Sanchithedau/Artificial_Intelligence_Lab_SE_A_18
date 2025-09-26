# Minimax Algorithm with Binary Tree Printing

class Node:
    def __init__(self, name, value=None, left=None, right=None):
        self.name = name      # Node label (A, B, etc.)
        self.value = value    # Leaf value (if any)
        self.left = left
        self.right = right


def minimax(node, depth, player):
    """Recursive Minimax implementation."""
    if depth == 0 or (node.left is None and node.right is None):
        return node.value

    if player == "MAX":
        alpha = float("-inf")
        if node.left:
            alpha = max(alpha, minimax(node.left, depth - 1, "MIN"))
        if node.right:
            alpha = max(alpha, minimax(node.right, depth - 1, "MIN"))
        return alpha
    else:  # MIN player
        alpha = float("inf")
        if node.left:
            alpha = min(alpha, minimax(node.left, depth - 1, "MAX"))
        if node.right:
            alpha = min(alpha, minimax(node.right, depth - 1, "MAX"))
        return alpha


def print_tree(node, level=0, prefix="Root: "):
    """Pretty print the binary tree."""
    if node is not None:
        print(" " * (4 * level) + prefix + f"{node.name}", end="")
        if node.value is not None:
            print(f" ({node.value})")  # Leaf value
        else:
            print()
        if node.left:
            print_tree(node.left, level + 1, "L--- ")
        if node.right:
            print_tree(node.right, level + 1, "R--- ")


# ------------------------------
# Build Example Binary Tree
# ------------------------------

# Leaf nodes with heuristic values
D = Node("D", value=2)
E = Node("E", value=4)
F = Node("F", value=5)
G = Node("G", value=8)

# Internal nodes
B = Node("B", left=D, right=E)  # Min node
C = Node("C", left=F, right=G)  # Min node

# Root
A = Node("A", left=B, right=C)  # Max node

# ------------------------------
# Print Tree
# ------------------------------

print("Binary Tree Structure:\n")
print_tree(A)

# ------------------------------
# Run Minimax
# ------------------------------

best_value = minimax(A, 2, "MAX")
print("\nBest achievable value for the maximizing player:", best_value)

