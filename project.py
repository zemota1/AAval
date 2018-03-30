import numpy.matlib as np
import math
import sys
import pprint
from operator import itemgetter, attrgetter


def diff(a, limit):

    dif = []
    size = len(a[0])-1
    print("size", size)
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            total = 0
            if(i!=j):
                for k in range (size):
                    if (a[i][k]!=a[j][k]):
                        total += 1
                if(total <= limit):
                    dif.append([i, j, total])
    print ("Diferenças: ")
    print (dif)

    final = sorted(dif,  key=lambda element: element[2])
    #sorted(dif,key=itemgetter(2,0,1))

    print("sorted")
    print(final)

    return final


def final(sorted):

    aux = []
    auxOutput = []

    for i in sorted:
        if i[1] not in aux:
            aux.append(i[1])
            auxOutput.append((i[0], i[1]))

    auxOutput.sort(key=itemgetter(0,1))

    for i in auxOutput:
        print(i[0]+1, i[1]+1)


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
