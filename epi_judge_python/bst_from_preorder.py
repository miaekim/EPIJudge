from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test


def rebuild_bst_from_preorder(preorder_sequence: List[int]
                              ) -> Optional[BstNode]:
    n = len(preorder_sequence)
    # print(preorder_sequence)
    if n <= 0:
        return None

    if n == 1:
        return BstNode(preorder_sequence[0])

    root = BstNode(preorder_sequence[0])
    
    transition_idx = n
    for idx in range(1, n):
        if preorder_sequence[idx] > preorder_sequence[0]:
            transition_idx = idx
            break
    
        
    root.left = rebuild_bst_from_preorder(preorder_sequence[1:transition_idx])
    root.right = rebuild_bst_from_preorder(preorder_sequence[transition_idx:])

    return root












    # root = BstNode(preorder_sequence[0])
    # to_visit = deque([(root, 0)])
    # while to_visit:
    #     node, node_idx = to_visit.pop()
    #     for idx in range(node_idx + 1, n):
    #         if preorder_sequence[idx] > node.data:
    #             node.right = BstNode(preorder_sequence[idx])
    #             to_visit.append((node.right, idx))
    #             break
        
    #     for idx in range(node_idx + 1, n):
    #         if preorder_sequence[idx] < node.data:
    #             node.left = BstNode(preorder_sequence[idx])
    #             to_visit.append((node.left, idx))
    #             break
        

        
    return None


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bst_from_preorder.py',
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
