import prim
import binheap
import graphy
import math

def main():

	v1 = [0, 0, None]
	
	v2 = [math.inf, 1, None]
	
	v3 = [math.inf, 2, None]
	
	v4 = [math.inf, 3, None]
	
	v5 = [math.inf, 4, None]
	
	v6 = [math.inf, 5, None]
	


	g = graphy.Graph(6)
	n1 = graphy.Edge(0, 1, 4)
	n11 = graphy.Edge(1, 0, 4)
	n2 = graphy.Edge(0, 5, 2)
	n22 = graphy.Edge(5, 0, 2)
	n3 = graphy.Edge(1, 2, 6)
	n33 = graphy.Edge(2, 1, 6)
	n4 = graphy.Edge(1, 5, 3)
	n44 = graphy.Edge(5, 1, 3)
	n5 = graphy.Edge(2, 5, 1)
	n55 = graphy.Edge(5, 2, 1)
	n6 = graphy.Edge(2, 3, 3)
	n66 = graphy.Edge(3, 2, 3)
	n8 = graphy.Edge(3, 4, 2)
	n88 = graphy.Edge(4, 3, 2)
	n9 = graphy.Edge(5, 4, 4)
	n99 = graphy.Edge(4, 5, 4)

	l1 = graphy.LinkedList()
	l1.append(n1)
	l1.append(n2)
	l2 = graphy.LinkedList()
	l2.append(n11)
	l2.append(n3)
	l2.append(n4)
	l3 = graphy.LinkedList()
	l3.append(n33)
	l3.append(n5)
	l3.append(n6)
	l4 = graphy.LinkedList()
	l4.append(n66)
	l4.append(n8)
	l5 = graphy.LinkedList()
	l5.append(n88)
	l5.append(n99)
	l6 = graphy.LinkedList()
	l6.append(n44)
	l6.append(n55)
	l6.append(n9)



	g.links[0] = l1
	g.links[1] = l2
	g.links[2] = l3
	g.links[3] = l4
	g.links[4] = l5
	g.links[5] = l6

	a = [v1, v2, v3, v4, v5, v6]

	bh = binheap.binheap(6)
	bh.binheap_make(6, a)

	prim.prim(0,g,bh)

main()