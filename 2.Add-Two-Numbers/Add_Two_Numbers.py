# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		first_value = self.get_int_value(l1)
		second_value = self.get_int_value(l2)
		value = first_value + second_value
        
		radix = 10
		prev = None
		head = None
		
		if value == 0:
			head = ListNode(0)
			return head

		while value > 0:
			node = ListNode(value % radix)
			if head is None:
				head = node

			if prev is None:
				prev = node
			else:
				prev.next = node
				prev = node

			value = value / radix
		
		return head 


	def get_int_value(self, head):
		radix = 1
		cur = head
		value = 0
		while cur is not None:
			value += cur.val * radix
			radix *= 10
			cur = cur.next

		return value