# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def indexOfNodeVal(self, node: 'Node', head: 'Node') -> 'Node':
        """Finds and returns the node in the list corresponding to the original node."""
        curr = head
        while curr:
            if curr == node:  # Match the exact node
                return curr
            curr = curr.next
        return None

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Create a mapping from original nodes to their copies
        old_to_new = {}
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)  # Create a copy of each node
            curr = curr.next

        # Step 2: Assign next and random pointers for the copied nodes
        curr = head
        while curr:
            old_to_new[curr].next = old_to_new.get(curr.next)  # Set the next pointer
            old_to_new[curr].random = old_to_new.get(curr.random)  # Set the random pointer
            curr = curr.next

        # Step 3: Return the copied head
        return old_to_new[head]
