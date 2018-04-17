import math
import binheap
import graphy


def prim(root, g, bh):

    n = g.size
    a = []

    vertices = [0, 1, 2, 3, 4 ,5]



    while (len(vertices) != 0):

            u = bh.binheap_top()
            vertices.remove(u[1])

            if (u[2] != None):

                a.append((u[2]+1, u[1]+1))

            adj = g.getLinksOfVertexV(u[1])
            aux = adj.getHead()
            while (aux != None):
                d = aux.getDest()
                v = aux.getVal()

                neighbour = bh.heap[bh.map[d]]
                if (d in vertices) and (v < neighbour[0]):
                    neighbour[2] = u[1]
                    neighbour[0] = v
                if (aux.getNext() == None):
                    break;
                else:
                    aux = aux.getNext()

            bh.binheap_delMin()

    return a
