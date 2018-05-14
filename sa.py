from sys import stdin, stdout
import math

def readInput(n):

    new = ''
    sa = []
    text = []
    while n > 0:
        new = stdin.readline()
        new = new[:-1]
        for i in range(len(new)):
            sa += [new[-i:]]
        n-=1

    suffix = sa

    return sorted(range(len(sa)), key=lambda k: sa[k]), suffix

def lcpFunc(sa, suffix):
    length = len(sa)
    lcp = [None]*length
    for i in range(0, length-1):
        lcp[i+1] = diff(sa, i, suffix)
    return lcp

def diff(sa, i, suffix):
    s1 = suffix[sa[i]]
    s2 = suffix[sa[i+1]]
    length = min(len(s1), len(s2))
    common = 0
    for j in range(length):
        if s1[j] == s2[j] :
            common += 1
        else: break
    return common

def test(sa, suffix, lcp, limit, n):

    length = len(suffix[0])
    k = limit + 1
    l = math.ceil(length/k)
    aux = []
    candidatesList = [[] for i in range(limit+1)]

    for i in range(1, len(lcp)):
        if lcp[i] >= l:
            aux += [i]
        else:
            if (len(aux) == 0):
                continue
            aux += [aux[0] - 1]
            candidatesList = candidates(sa, suffix, lcp, aux, l, k, candidatesList)
            aux = []

    return candidatesList


def candidates(sa, suffix, lcp, aux, l, k, candidatesList):

    length = len(suffix[0])
    seq = []

    for i in range (len(aux)):
        for j in range (i+1, len(aux)):
            first = sa[aux[i]]
            second = sa[aux[j]]
            if((len(suffix[first]) == len(suffix[second])) and ((length - len(suffix[first])) % l) == 0):
                nr_set = int((len(suffix[first]) -1 ) / l)
                candidatesList[nr_set].append([suffix[first - first % length], (first - first % length)/length])
                candidatesList[nr_set].append([suffix[second - second % length], (second - second % length)/length])

    return candidatesList

def hamming(candidatesList, limit, size):

    for i in candidatesList:
        for j in range(len(i)):
            for h in range(j+1, len(i)):
                total = 0
                for k in range (size):
                    if (i[j][0][k]!=i[h][0][k]): #limit
                        total += 1
                        if (total > limit):
                            break
                if(total <= limit):
                    e1 = (i[j][1],i[h][1],total)
                    print(e1)                        #g.append(i,e1)
                    #g.append(j,e2)

def main():

    n = int(stdin.readline())
    sa, suffix = readInput(n)
    limit = int(stdin.readline())
    size = len(suffix[0])
    print(sa, '\n\n',suffix)
    lcp = lcpFunc(sa, suffix)
    print(lcp)
    candidatesList = test(sa, suffix, lcp, limit, n)
    hamming(candidatesList, limit,size)


main()
