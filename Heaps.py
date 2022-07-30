import math
from typing import TypeVar, Generic

T = TypeVar('T')


class Heap():

	def __init__(self, arr, n):
		self.heap_size = len(arr)
		self.A = arr
		self.n = n
		i = 0
		while (i < n - self.heap_size):
			self.A.append(None)
			i += 1

	@staticmethod
	def left(i) -> int:
		return (2 * i + 1)

	@staticmethod
	def right(i) -> int:
		return (2 * i + 2)
	
	@staticmethod
	def parent(i) -> int:
		return math.floor((i - 1) / 2)

	def less(self, i, j) -> bool:
		if (self.A[i] < self.A[j]):
			return True
		else:
			return False

	def exchange(self, i, j):
		self.A[i], self.A[j] = self.A[j], self.A[i]

	def print(self):
		print("[", end=" ")
		for i in range(0, self.heap_size):
			print(self.A[i], end=', ')
		print("] ")

	def build_max_heap(self):
		c = math.floor(self.heap_size / 2)
		for i in range(c - 1, -1, -1):  # stop bound is non-inclusive in Python
			self.max_heapify_sink(i)

	def build_min_heap(self):
		c = math.floor(self.heap_size / 2)
		for i in range(c - 1, -1, -1):  # stop bound is non-inclusive in Python
			self.min_heapify_sink(i)

	def max_heapify_sink(self, i):
		'''Bottom-up reheapify'''
		l = Heap.left(i)  # left of A[i]
		r = Heap.right(i)  # right of A[i]
		# determines the largest of the elements A[i], A[LEFT(i)], and A[RIGHT(i)] and stores the index of the largest element in largest.
		if (l < self.heap_size and self.less(i, l)):
			largest = l
		else:
			largest = i
		if (r < self.heap_size and self.less(largest, r)):
			largest = r
			'''
			If A[i] is largest, then the subtree rooted at node i is already a max-heap and nothing else needs to be done.
			Otherwise, one of the 2 children contains the largest element.
			Positions i and largest swap their contents, which causes node i and its children to satisfy the max-heap property.
			The node indexed by largest, however, just had its value decreased, and thus the subtree rooted at largest might violate the max-heap property.
			Consequently, MAX-HEAPIFY calls itself recursively on that subtree.
		'''

		if largest != i:
			self.exchange(i, largest)
			self.max_heapify_sink(largest)

	# TODO:iterative max_heapify
	def max_heapify_swim(self, i):
		while (i > 0 and self.less(Heap.parent(i), i)):
			self.exchange(Heap.parent(i), i)
			i = Heap.parent(i)

	def min_heapify_sink(self, i):
		l = Heap.left(i)  # left of A[i]
		r = Heap.right(i)  # right of A[i]
		# determines the smallest of the elements A[i], A[LEFT(i)], and A[RIGHT(i)] and stores the index of the smallest element in 'smallest'.
		if (l < self.heap_size and self.less(l, i)):
			smallest = l
		else:
			smallest = i

		if (r < self.heap_size and self.less(r, smallest)):
			smallest = r
			'''
			If A[i] is smallest, then the subtree rooted at node i is already a min-heap and nothing else needs to be done.
			Otherwise, one of the 2 children contains the smallest element.
			Positions i and smallest swap their contents, which causes node i and its children to satisfy the min-heap property.
			The node indexed by smallest, however, just had its value icreased, and thus the subtree rooted at smallest might violate the min-heap property.
			Consequently, MIN-HEAPIFY calls itself recursively on that subtree.
		'''
		if smallest != i:
			self.exchange(i, smallest)
			self.min_heapify_sink(smallest)

	def min_heapify_swim(self, i):
		while (i > 0 and self.less(i, Heap.parent(i))):
			self.exchange(Heap.parent(i), i)
			i = Heap.parent(i)

	def heap_sort(self):
		self.build_max_heap()
		a = []
		for i in range(self.heap_size - 1, 0, -1):
			a.insert(0, self.A[0])
			self.exchange(0, i)
			self.heap_size -= 1
			# print(self.A[i], end=', ')
			self.max_heapify_sink(0)
		print(a)

	def max_heap_insert(self, *keys):
		for k in keys:
			if (self.heap_size + 1 >= self.n):
				print("Heap overflow")
				return
			self.heap_size += 1
			x = self.A[self.heap_size - 1] = -4545435454325454
			self.max_heap_increase_key(x, k)
			self.print()

	def max_heap_increase_key(self, x, k):
		if (x > k):
			print("New key is less than the existing key")
			return
		foundat = -1
		for i in range(0, self.heap_size):
			if (self.A[i] == x):
				foundat = i
				break
		if (foundat < 0):
			return
		self.A[foundat] = k
		self.max_heapify_swim(foundat)

	def max_heap_extract_max(self) -> int:
		maxk = self.max_heap_peek_max()
		self.A[0] = self.A[self.heap_size - 1]
		self.heap_size -= 1
		self.max_heapify_sink(0)
		return maxk

	def max_heap_peek_max(self) -> int:
		if (self.heap_size <= 0):
			print("Heap underflow")
			return -4545435454325454
		return self.A[0]


heap2 = Heap([27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0], 30)
heap2.build_max_heap()
heap2.print()
#heap2.heap_sort()
heap2.build_min_heap()
heap2.print()
print("-----------------------------------")
heap1 = Heap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7], 20)
heap1.build_max_heap()
heap1.print()

heap1.max_heap_insert(5, 34, 32, 54, 86, 94, -56)
heap1.print()
#print(heap1.max_heap_extract_max())
#heap1.print()
