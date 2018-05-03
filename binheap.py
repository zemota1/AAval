#!/usr/bin/python3
import math

def left(x):
	return ((((x) + 1) << 1) - 1)

def right(x):
	return (((x) + 1) << 1)

def parent(x):
	return ((((x) + 1) >> 1) - 1)

def cmp(a, b):

	for i in [1,2]:
		if(a[i] == None):
			a[i] = math.inf
		if(b[i] == None):
			b[i] = math.inf

	vertex = {"head":[a[1], a[2]], "neighbour": [b[1], b[2]]}
	if (a[0] < b[0]):
		return True
	elif (a[0] == b[0]):
		if (min(vertex["head"]) < min(vertex["neighbour"]) ):
			return True
		elif((min(vertex["head"]) == min(vertex["neighbour"]))):
			if (max(vertex["head"]) < max(vertex["neighbour"]) ):
				return True
	return False


class binheap:


	def __init__(self, n):
		self.size = 0
		self.heap = [None]*n
		self.map = [None]*n
		self.vertices = {}
		for i in range(n):
			self.vertices[i] = True

	def heapPrint(self):
		return self.heap

	def binheap_empty(self):
		if(self.size == 0):
			return True

		return False

	def binheap_top(self):
		return self.heap[0]

	def binheap_insert(self, v):

		self.heap.append(v)
		self.map[v[1]] = self.size
		self.vertices[self.size] = True
		self.size += 1

		self.binheap_siftup(self.heap, self.size-1)
		self.binheap_siftdown(self.heap,0)


	def binheap_delMin(self):

		aux = self.heap[0]
		self.size -=1
		self.binheap_exchange(self.heap, self.size, 0)
		self.binheap_siftdown(self.heap, 0)

		del self.heap[-1]

		self.vertices[aux[1]] = False

		self.map[aux[1]] = -1

	def binheap_make(self, n, list):
		self.size = n
		self.heap = list[:]
		for i in range(n):
			self.map[self.heap[i][1]] = i

		for i in range (parent(n - 1), -1, -1):
			self.binheap_siftdown(self.heap, i)

	def binheap_exchange(self, heap, i, j):

		self.map[heap[i][1]] = j
		self.map[heap[j][1]] = i
		aux = heap[i]
		self.heap[i] = heap[j]
		self.heap[j] = aux


	def binheap_siftdown(self, heap, start):

		l = left(start)
		r = right(start)
		m = start

		if(l < self.size and cmp(heap[l], heap[m])):
			m = l
		if(r < self.size and cmp(heap[r], heap[m])):
			m = r
		if(m == start):
			return

		self.binheap_exchange(heap, start, m)
		self.binheap_siftdown(heap, m)

	def binheap_siftup(self, heap, start):

		p = parent(start)

		if((p>=math.inf) or (p<0) or cmp(self.heap[p], self.heap[start])):
			return

		self.binheap_exchange(heap, start, p)
		self.binheap_siftup(self.heap, p)
