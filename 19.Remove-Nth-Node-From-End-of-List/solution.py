# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def removeNthFromEnd(self, head, n):
		"""
		用两个指针，第一个指针指向比第二个指针快n个节点，
		则当第一个指针指向最后一个节点时，第二个指针指向被删除节点的前一个节点
		:type head: ListNode
		:type n: int
		:rtype: ListNode
		"""
		first_pointer = head
		second_pointer = head
		for i in range(0,n):
			first_pointer = first_pointer.next

		print(first_pointer.val)
		
		# 删除的是第一个节点
		if first_pointer is None:
			return head.next
		
		while True:
			if first_pointer.next is None:
				break
			first_pointer = first_pointer.next
			second_pointer = second_pointer.next
		
		second_pointer.next = second_pointer.next.next
		
		return head
