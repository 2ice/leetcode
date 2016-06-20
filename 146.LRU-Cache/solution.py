# -*- coding:utf-8 -*-
class LRUCache(object):
	"""
	使用字典加双向队列实现：
	"""

	def __init__(self, capacity):
		"""
		:type capacity: int
		"""
		self.__capacity = capacity
		self.__cache = {}
		self.__head = None
		self.__tail = None

	def get(self, key):
		"""
		:rtype: int
		"""
		if key in self.__cache:
			value = self.__cache[key].value

			self.__move_to_first(key)
			return value
		else:
			return -1

	def set(self, key, value):
		"""
		:type key: int
		:type value: int
		:rtype: nothing
		"""
		if key in self.__cache:
			self.__cache[key].value = value

			self.__move_to_first(key)
		else:
			if self.__capacity <= 0:
				return

			node = Node()
			node.key = key
			node.value = value
			node.next = self.__head

			if self.__head is not None:
				self.__head.prev = node

			self.__head = node

			if self.__tail is None:
				self.__tail = node

			self.__cache[key] = node

			self.__remove_last_node_if_full()

	def __move_to_first(self, key):
		"""
		把key所在的节点移到列表的第一个元素
		"""
		if key not in self.__cache:
			return

		cur = self.__cache[key]
		if cur.prev is None:
			# 说明是列表的第一个节点，不需要操作，返回
			return

		if cur == self.__tail:
			self.__tail = cur.prev

		cur.prev.next = cur.next
		if cur.next is not None:
			cur.next.prev = cur.prev

		cur.next = self.__head
		self.__head.prev = cur
		cur.prev = None
		self.__head = cur

	def __remove_last_node_if_full(self):
		if len(self.__cache) <= self.__capacity:
			return

		last_node = self.__tail

		self.__tail = self.__tail.prev

		self.__tail.next = None
		del self.__cache[last_node.key]
		del last_node


class Node(object):
	def __init__(self):
		self.prev = None
		self.next = None
		self.value = None
		self.key = None
