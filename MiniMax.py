def minimax(node, depth, maximizingPlayer, values):
    if depth == 0 or node is None:
        return values[node]
    if maximizingPlayer:
        maxEval = float('-inf')
        for child in children(node):
            eval = minimax(child, depth - 1, False, values)
            maxEval = max(maxEval, eval)
        return maxEval
    else:
        minEval = float('inf')
        for child in children(node):
            eval = minimax(child, depth - 1, True, values)
            minEval = min(minEval, eval)
        return minEval

def children(node):
    # Returns the children of a given node
    return ...

def values(node):
    # Returns the value of a given node
    return ...

if __name__ == '__main__':
    root = ...  # The root node of the game tree
    depth = ...  # The maximum depth of the search
    bestEval = minimax(root, depth, True, values)
    print("The best evaluation is:", bestEval)
