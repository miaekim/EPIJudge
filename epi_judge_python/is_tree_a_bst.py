from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def is_binary_tree_bst_with_bound(tree: BinaryTreeNode, lower_bound, upper_bound) -> bool:
    if not tree:
        return True

    left = is_binary_tree_bst_with_bound(tree.left, lower_bound, tree.data)
    if not left or (tree.left and tree.left.data < lower_bound):
        return False
    right = is_binary_tree_bst_with_bound(tree.right, tree.data, upper_bound)
    if not right or (tree.right and tree.right.data > upper_bound):
        return False

    okay_left = False
    if not tree.right or (tree.right and tree.data <= tree.right.data):
        okay_left = True

    okay_right = False
    if not tree.left or (tree.left and tree.data >= tree.left.data):
        okay_right = True

    return okay_left and okay_right
    
        
    

def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    return is_binary_tree_bst_with_bound(tree, float('-inf'), float('inf'))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
