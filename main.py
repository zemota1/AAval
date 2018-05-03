#!/usr/bin/python3

import prim
import binheap
import graphy
import math
import read
from sys import stdin, stdout


def main():

	n = int(stdin.readline())

	g = graphy.Graph(n)
	text = read.readInput(n)
	limit = int(stdin.readline())

	g = read.diff(text, limit, g)

	vertices = read.inputHeap(n, limit)
	bh = binheap.binheap(n)
	bh.binheap_make(n, vertices)

	min = prim.prim(g,bh)
	for i in min:
		stdout.write(str(i[0]) + ' ' + str(i[1]) + '\n')

main()
