#!/usr/bin/python3
'''
class Edge:
	def __init__(self, source, dest, val):
		self.source = source
		self.val = val
		self.dest = dest
		self.next = None

	def getVal(self):
		return self.val

	def getDest(self):
		return self.dest

	def getSource(self):
		return self.source

	def setVal(self, val):
		self.val = val

	def setDest(self, dest):
		self.dest = dest

	def setSource(self, source):
		self.source = source

	def getNext(self):
		return self.next

	def setNext(self, next):
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None

	def getHead(self):
		return self.head

	def setHead(self, head):
		self.head = head

	def append(self, item):
		current = self.head
		if current:
			while current.getNext()!= None:
				current = current.getNext()
			current.setNext(item)
		else:
			self.head = item

	def hasElem(self, val):
		current = self.head
		if current:
			while current.getNext()!= None:
				if(current.getNext().getVal(val) == val):
					return True
				current = current.getNext()
			return False
		return False

	def displayList(self):
		current = self.head
		if current:
			while current.getNext()!= None:
				print(current.getVal())
				current = current.getNext()
			print(current.getVal())
'''


class Graph:
	def __init__(self, size):

		self.links = [[]]*size
		for i in range(size):
			self.links[i] = []
		self.size = size


	def append(self, source, item):
		self.links[source].append(item)

	def getLinksOfVertexV(self, vertexId):
		return self.links[vertexId]
