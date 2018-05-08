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

    length = len(sa[0])
    k = limit + 1
    l = math.ceil(length/k)


    for i in range(len(lcp)):
        aux = []
        if lcp[i] >= l:
            aux += i
        else:
            aux += aux[0]-1
            candidates(sa, suffix, lcp, aux, length, k)

def candidates(sa, suffix, lcp, aux, length):
    candidates = []

    seq = []
    for i in range(k):
        seq += [i]
    dict = dict.fromkeys(seq, [])

    for i in range(0, len(aux)):
        for j in range(i+1, len(aux)):
            first = sa[i]
            second = sa[j]
            if((suffix[first] % length) == (suffix[second] % length)):
                nr_set = (suffix[first] % length) / length
                dict[nr_set].append(suffix[first - first % length])
                dict[nr_set].append(suffix[second - second % length])

def main():

    n = int(stdin.readline())
    sa, suffix = readInput(n)
    limit = int(stdin.readline())
    print(sa, '\n\n',suffix)
    lcp = lcpFunc(sa, suffix)
    test(sa, suffix, lcp, n, limit)

main()
