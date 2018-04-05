import math

def prim(root, n):

    a = []
    key = [(math.inf)]*n #numero de vertices
    parent = [(None)]*n

    #test
    adj = {0: [(1,4),(5,2)], 1: [(0,4),(2,6),(5,3)], 2: [(1,6), (3,3), (5,1)], 3: [(2,3),(4, 2)], 4: [(3,2), (5,4)], 5: [(0,2), (1,3), (2,1), (4, 4)]} #a:0 ; b:1 ; c:2 ; d:3 ; e: 4 ; f:5
    vertices = [0, 1, 2, 3, 4 ,5] #
    key[root] = 0

    while (len(vertices) != 0):

            u = key.index(min(key)) #vamos utilozar hip?
            key[u] = math.inf
            print(key)
            print(u)
            vertices.remove(u)


            print ('Depois do remove' , vertices)

            if (parent[u] != None):
                a.append((u, parent[u]))

            for i in adj.get(u):
                if (i[0] in vertices) and (i[1] < key[i[0]]):
                    parent[i[0]] = u
                    key[i[0]] = i[1]

    print(a)

prim(0, 6)
