"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head):
        dict1 = {}

        def dfs(node):
            if not node:
                return None

            if node in dict1:
                return dict1[node]

            temp = Node(node.val, next = None, random = None)
            dict1[node] = temp
            temp.next = dfs(node.next)
            temp.random = dfs(node.random)

            return dict1[node]

        return dfs(head)
