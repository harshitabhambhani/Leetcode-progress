# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head):
        # Helper function to reverse a linked list
        def reverseLinkedList(node):
            prev = None
            while node:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
            return prev

        # Helper function to find the maximum twin sum
        def findMaxTwinSum(first, second):
            maxSum = float('-inf')
            while first and second:
                twinSum = first.val + second.val
                maxSum = max(maxSum, twinSum)
                first = first.next
                second = second.next
            return maxSum

        # Find the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        # Divide the linked list into two halves
        middle = length // 2
        firstHalfEnd = head
        for _ in range(middle - 1):
            firstHalfEnd = firstHalfEnd.next

        # Reverse the second half
        secondHalfStart = reverseLinkedList(firstHalfEnd.next)

        # Find the maximum twin sum
        maxSum = findMaxTwinSum(head, secondHalfStart)

        # Restore the linked list to its original state (reverse the second half again)
        firstHalfEnd.next = reverseLinkedList(secondHalfStart)

        return maxSum

# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6
linked_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))

# Instantiate the solution class
solution = Solution()

# Find and print the maximum twin sum
print(solution.pairSum(linked_list))
