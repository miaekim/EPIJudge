from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    if not preorder:
        return None
    root = BinaryTreeNode(preorder[0])
    if len(preorder) >  1:
        idx = inorder.index(root.data)
        root.left = binary_tree_from_preorder_inorder(preorder[1:1+idx],inorder[:idx])
        root.right = binary_tree_from_preorder_inorder(preorder[1+idx:],inorder[idx+1:])
    return root


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
