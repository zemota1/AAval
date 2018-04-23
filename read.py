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
        for j in range(length):
            total = 0
            if(i!=j):
                for k in range (size):
                    if (a[i][k]!=a[j][k]): #limit
                        total += 1
                    if (total > limit):
                        break
                if(total <= limit):
                    '''if(i == 16):
                                                                                    print(i,j,total)'''
                    e1 = graphy.Edge(i,j,total)
                    l.append(e1)
        g.links[i] = l

    return g

def inputHeap(n, limit):
    array = [[0,0,None]]

    for i in range(1,n):
        array.append([limit+1, i, None])

    return array
