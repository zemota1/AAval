import math
import binheap
import graphy


def prim(root, g, bh):

    n = g.size
    a = []

    vertices = [0, 1, 2, 3, 4 ,5]

  

    while (len(vertices) != 0):

            u = bh.binheap_min()
            print('Vertices', vertices)
            print('u min', u)
            vertices.remove(u[1])
            print('vertices remove u', vertices)

            if (u[2] != None):

                a.append((u[1], u[2]))

            adj = g.getLinksOfVertexV(u[1])
            #adj.displayList()
            aux = adj.getHead()
            while (aux != None):
                d = aux.getDest()
                v = aux.getVal()
                print('D', d)
                print('V', v)
                neighbour = bh.heap[bh.map[d]]
                print('neig', type(bh.heap[bh.map[d]]))
                if (d in vertices) and (v < neighbour[0]):
                    neighbour[2] = u[1]
                    neighbour[0] = v
                if (aux.getNext() == None):
                    break;
                else:        
                    aux = aux.getNext()

                print('---------------')
            print('§§§§§§§§§§§§') 

    return a



