#!/usr/bin/python3

import binheap
import graphy
import math


def prim(g, bh):

    mst = []


    while(1):
        u = bh.binheap_top()
        if (u[2] != (None or math.inf)):
            minn = min(u[2]+1, u[1]+1)
            maxx = max(u[2]+1, u[1]+1)
            mst.append([minn, maxx])

        bh.binheap_delMin()

        if(bh.binheap_empty()):
            break

        adj = g.getLinksOfVertexV(u[1])
        i = 0
        if(len(adj)==0):
            aux = False
        else:
            aux = True

        while (aux and i < len(adj)):
            d = adj[i][1]
            v = adj[i][2]
            head1 = [v, u[1], d]
            head2 = [v, d, u[1]]

            neighbour = bh.heap[bh.map[d]]

            if (bh.vertices[d]) and (binheap.cmp(head1, neighbour) or binheap.cmp(head2, neighbour)):
                neighbour[2] = u[1]
                neighbour[0] = v
                bh.binheap_siftup(bh.heap, bh.map[d])

            i+=1




    mst = sorted(mst, key = lambda x: (x[0], x[1]))

    return mst
