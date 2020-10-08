from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

import queue

def is_symmetric(tree: BinaryTreeNode) -> bool:
    if tree == None:
        return True

    left_q = queue.Queue()
    if tree.left != None:
        left_q.put(tree.left)
    right_q = queue.Queue()
    if tree.right != None:
        right_q.put(tree.right)

    while left_q.empty() == False and right_q.empty() == False:
        l = left_q.get()
        r = right_q.get()

        if l.data != r.data:
            return False

        if l.left != None:
            left_q.put(l.left)
        if l.right != None:
            left_q.put(l.right)

        if r.right != None:
            right_q.put(r.right)
        if r.left != None:
            right_q.put(r.left)

    if left_q.empty() == True and right_q.empty() == True:
        return True
    else:
        return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
