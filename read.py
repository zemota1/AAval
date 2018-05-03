#!/usr/bin/python3

import graphy

from sys import stdin, stdout


def readInput(n):

    a = []
    while n > 0:

        reader = stdin.readline()
        a.append(reader)
        n-=1

    return a



def diff(a, limit, g):

    size = len(a[0])
    length = len(a)
    for i in range(length):
        for j in range(i+1,length):
            total = 0
            for k in range (size):
                if (a[i][k]!=a[j][k]): #limit
                    total += 1
                    if (total > limit):
                        break
            if(total <= limit):
                e1 = (i,j,total)
                e2 = (j,i,total)
                g.append(i,e1)
                g.append(j,e2)

    return g


def inputHeap(n, limit):

    array = [[0,0,None]]

    for i in range(1,n):
        array.append([limit+1, i, None])

    return array
