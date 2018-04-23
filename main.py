import prim
import binheap
import graphy
import math
import read

def main():

	n = int(input())

	g = graphy.Graph(n)
	text = read.readInput(n)
	limit = int(input())

	g = read.diff(text, limit, g)

	vertices = read.inputHeap(n, limit)
	bh = binheap.binheap(n)
	bh.binheap_make(n, vertices)

	min = prim.prim(g,bh,n)
	for i in min:
		print(i[0], i[1])

main()