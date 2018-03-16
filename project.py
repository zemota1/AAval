import numpy.matlib as np
import math
import sys
import pprint

'''
class Graph(object):

    def __init__(self, connections):
        self.graph = {}
        self.addConnections(connections)

    def addConnections(self, connections):

        for i in connections:
            self.graph[i[0]] = [i[1], i[2]]

'''

def diff(a, limit):

    dif = []
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            total = 0
            if(i!=j):
                for k in range (len(a[0])):
                    if (a[i][k]!=a[j][k]):
                        total += 1
                if(total <= limit):
                    dif.append([i, j, total])

    sorted = np.array(dif)
    sorted[:,2].sort()

    return sorted

def final(sorted):

    aux = []
    for i in sorted:
        if i[1] not in aux:
            aux.append(i[1])
            print (int(i[0])+1, ' ', int(i[1])+1)


def readInput(n):


    a = []
    while n > 0:

        reader = input()
        a.append(reader)
        n-=1

    return a


def main():

    n = int(input())
    text = readInput(n)
    limit = int(input())


    dif = diff(text, limit)

    final(dif)


main()
