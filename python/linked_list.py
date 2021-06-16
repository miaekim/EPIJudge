from typing import List


class ListNode:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next

def search_list(L:ListNode, key: int):
    while L and L.data != key:
        L = L.next
    return L

def insert_after(node:ListNode, new_node:ListNode):
    new_node.next = node.next
    node.next = new_node

def delete_after(node:ListNode):
    node.next = node.next.next
    