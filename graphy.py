class Edge:
	def __init__(self, source, dest, weight):
		self.source = source
		self.dest = dest
		self.weight = weight
	

class Node:
	def __init__(self, val):
		self.parent = None
		self.val = val
		self.next = None
	
	def getVal(self):
		return self.val

	def getNext(self):
		return self.next
	
	def getParent(self):
		return self.parent
	
	def setVal(self, val):
		self.val = val

	def setNext(self, next):
		self.next = next
	
	def setParent(self, parent):
		self.parent = parent
		
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
			current.setNext(Node(item))	
		else:
			self.head = Node(item)
	
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
	def getLinksOfVertexV(self, vertexId):
		return self.links[vertexId]	



g = Graph(10)
l1 = LinkedList()
l1.append(10)
l1.append(20)
l1.append(30)
l2 = LinkedList()
l2.append(70)
l2.append(20)
l2.append(30)
l2.append(50)
l2.append(40)
g.links[0] = l1
g.links[1] = l2
g.getLinksOfVertexV(1).displayList()
