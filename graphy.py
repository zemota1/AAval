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



class Graph:
	def __init__(self, size):
		self.links = [LinkedList]*size
		self.size = size
	def getLinksOfVertexV(self, vertexId):
		return self.links[vertexId]



g = Graph(6)
n1 = Edge('A', 'B', 4)
n11 = Edge('B', 'A', 4)
n2 = Edge('A', 'F', 2)
n22 = Edge('F', 'A', 2)
n3 = Edge('B', 'C', 6)
n33 = Edge('C', 'B', 6)
n4 = Edge('B', 'F', 3)
n44 = Edge('F', 'B', 3)
n5 = Edge('C', 'F', 1)
n55 = Edge('F', 'C', 1)
n6 = Edge('C', 'D', 3)
n66 = Edge('D', 'C', 3)
n8 = Edge('D', 'E', 2)
n88 = Edge('E', 'D', 2)
n9 = Edge('F', 'E', 4)
n99 = Edge('E', 'F', 4)

l1 = LinkedList()
l1.append(n1)
l1.append(n2)
l2 = LinkedList()
l2.append(n11)
l2.append(n3)
l2.append(n4)
l3 = LinkedList()
l3.append(n33)
l3.append(n5)
l3.append(n6)
l4 = LinkedList()
l4.append(n66)
l4.append(n8)
l5 = LinkedList()
l5.append(n88)
l5.append(n99)
l6= LinkedList()
l6.append(n44)
l6.append(n55)
l6.append(n9)



g.links[0] = l1
g.links[1] = l2
g.links[2] = l3
g.links[3] = l4
g.links[4] = l5
g.links[5] = l6


