import numpy.matlib as np
import math
import sys


def diff(a, counter):

    for i in range(len(a)):
        for j in range(len(a)):
            if(i!=j):
                for k in range (len(a[0])):
                    if (a[i][k]!=a[j][k]):
                        counter[i][j] += + 1



def putEdges(counter, result):

    for i in range(len(counter[0])):
        min = sys.maxsize
        idx = -1
        for j in range(len(counter[0])):
            if ((0 < counter[i][j] < min) and i!=j):
                min = counter[i][j]
                idx = j
        if (idx != -1):
            result[i][idx] = True
            print (idx+1, " ", i+1)
'''
def readInput(n):


    a = list()
    while n > 0:

        reader = input()
        a += list(reader)
        n-=1

    return a

'''
def main():
    '''
    n = int(input())
    text = readInput(n)

    esta a dar erro
'''

    text = ["0000000", "0001000", "1000000", "1011000", "0000111","1000111"]

    counter =  np.full((7,7), 0, dtype=int)

    result = np.full((7,7), 0, dtype=int)

    diff(text, counter)

    #print (counter)

    putEdges(counter, result)

    #print (result)


main()
