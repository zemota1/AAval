import math
import binheap
import graphy


def prim(g, bh, n):

    n = g.size
    mst = []


    while (not(bh.binheap_empty())):
            u = bh.binheap_top()
            if (u[2] != None):
                minn = min(u[2]+1, u[1]+1)
                maxx = max(u[2]+1, u[1]+1)
                mst.append([minn, maxx])
                #print([minn, maxx])
            
            bh.binheap_delMin()
            if(bh.binheap_empty()):
                break

            adj = g.getLinksOfVertexV(u[1])
            aux = adj.getHead()
            while (aux != None):
                d = aux.getDest()
                v = aux.getVal()
                neighbour = bh.heap[bh.map[d]]

                if (d in bh.vertices) and (v < neighbour[0]):
                    neighbour[2] = u[1]
                    neighbour[0] = v
                    bh.binheap_siftup(bh.heap, bh.map[d])

                if (aux.getNext() == None):
                    break;
                else:
                    aux = aux.getNext()
                
    mst = sorted(mst, key = lambda x: (x[0], x[1]))
    
    return mst
