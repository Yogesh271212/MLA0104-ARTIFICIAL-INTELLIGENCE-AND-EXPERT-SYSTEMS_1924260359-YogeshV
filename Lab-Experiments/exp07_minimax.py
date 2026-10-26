import math

def minimax(depth, node_index, is_max, scores, max_depth):
    if depth == max_depth:
        return scores[node_index]

    if is_max:
        return max(
            minimax(depth + 1, node_index * 2, False, scores, max_depth),
            minimax(depth + 1, node_index * 2 + 1, False, scores, max_depth)
        )
    else:
        return min(
            minimax(depth + 1, node_index * 2, True, scores, max_depth),
            minimax(depth + 1, node_index * 2 + 1, True, scores, max_depth)
        )

scores = [3, 5, 2, 9, 12, 5, 23, 23]
tree_depth = int(math.log(len(scores), 2))
optimal_value = minimax(0, 0, True, scores, tree_depth)
print("Leaf Node Scores:", scores)
print("Optimal Move Value:", optimal_value)
