class Node:
	def _init_(self, val):
		self.val = val;
		self.next = None
	
	def getVal(self):
		return self.val

	def getNext(self):
		return self.next	


	def setVal(self, val):
		self.val = val

	def setNext(self, next):
		self.next = next
			
class LinkedList:
	def _init_(self):
		self.head = None
	def append(self, item):
		current = self.head
		if current:
			while current.getNext()!= None:
				current = current.getNext()
			current.setNext(Node(item))	
		else
			self.head = Node(item)
	def hasElem(self, val):
		current = self.head
		if current:
			while current.getNext()!= None:
				if(current.getNext().getVal(val) == val)
					return True
				current = current.getNext()	
			return False	
		return False
		
class Graph:
	def _init_(self, size):
		self.links = [LinkedList]*size 	
	def getLinksOfVertexV(self, vertexId):
		return self.links[vertexId]	



def main:
	Graph g = Graph(10)
	Node n1 = Node(10)
	Node n2 = Node(20)
	Node n3 = Node(30)
	Node n4 = Node(40)
	Node n5 = Node(50)
	LinkedList l1 = LinkedList()
	l1.append(n1)
	l1.append(n2)
	l1.append(n3)
	LinkedList l2 = LinkedList()
	l1.append(n1)
	l1.append(n4)
	l1.append(n5)
	l1.append(n2)
	l1.append(n3)
	if(l1.hasElem(40))
		print "oi"

if __name__ == "__main__":
    main()
