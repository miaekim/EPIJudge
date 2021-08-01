import functools

from bst_node import BstNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook


def pair_includes_ancestor_and_descendant_of_m(possible_anc_or_desc_0: BstNode,
                                               possible_anc_or_desc_1: BstNode,
                                               middle: BstNode) -> bool:
    # node 0 or node 1 try to find middle. 
    # both find/cannot find -> return False
    # one find. -> okay then middle find other node -> if found True, else False

    def find_middle(root: BstNode, middle: BstNode) -> bool:
        if root.data == middle.data:
            return False
        node = root
        while node:
            if middle.data < node.data:
                node = node.left
            elif middle.data > node.data:
                node = node.right
            else:
                return True
        return False

    node_0_find_max = find_middle(possible_anc_or_desc_0, middle)
    node_1_find_max = find_middle(possible_anc_or_desc_1, middle)

    if node_0_find_max and not node_1_find_max:
        return find_middle(middle, possible_anc_or_desc_1)

    if node_1_find_max and not node_0_find_max:
        return find_middle(middle, possible_anc_or_desc_0)

    return False


@enable_executor_hook
def pair_includes_ancestor_and_descendant_of_m_wrapper(executor, tree,
                                                       possible_anc_or_desc_0,
                                                       possible_anc_or_desc_1,
                                                       middle_idx):
    candidate0 = must_find_node(tree, possible_anc_or_desc_0)
    candidate1 = must_find_node(tree, possible_anc_or_desc_1)
    middle_node = must_find_node(tree, middle_idx)

    return executor.run(
        functools.partial(pair_includes_ancestor_and_descendant_of_m,
                          candidate0, candidate1, middle_node))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'descendant_and_ancestor_in_bst.py',
            'descendant_and_ancestor_in_bst.tsv',
            pair_includes_ancestor_and_descendant_of_m_wrapper))
