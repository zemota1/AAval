import math
import graphy


def readInput(n):


    a = []
    while n > 0:

        reader = input()
        a.append(reader)
        n-=1

    return a

def diff(a, limit, g):
    size = len(a[0])
    length = len(a)
    for i in range(length):
        l = graphy.LinkedList()
        for j in range(i+1, len(a)):
            total = 0
            if(i!=j):
                for k in range (size-1):
                    if (a[i][k]!=a[j][k]): #limit
                        total += 1
                    if (total > limit):
                        break
                if(total <= limit):
                    e1 = graphy.Edge(i,j,total)
                    e2 = graphy.Edge(j,i,total)
                    l.append(e1)
                    l.append(e2)
        g.links[i] = l

    return g

def inputHeap(n, limit):
    array = [[0,0,None]]

    for i in range(1,n):
        array.append([limit+1, i, None])

    return array
