import math

def left(x):
    return ((((x) + 1) << 1) - 1)

def right(x):
    return (((x) + 1) << 1)

def parent(x):
    return ((((x) + 1) >> 1) - 1)

def cmp(a, b):

    if (a < b):
        return True
    if (a > b):
        return False
    #if (a == b):
    #    print ('VERRRRR')

class binheap:


    def __init__(self, n):
        self.size = 0
        self.heap = [None]*n
        #self.map = [None]*n


    def binheap_empty(self):
        if(self.size == 0):
            return True

        return False

    def binheap_top(self):
        return self.heap[0]

    def binheap_insert(self, id):

        self.heap.append(id)
        self.size += 1

        print("Heap com novo elemento", self.heap)
        self.binheap_siftup(self.heap, self.size-1)


    def binheap_min(self):

        aux = self.heap[0]
        self.size -=1

        self.binheap_exchange(self.heap, self.size, 0)
        self.binheap_siftdown(self.heap, 0)

        del self.heap[-1]
        print(self.heap)
        return aux

    def binheap_make(self, n, list):
        self.size = n

        self.heap = list[:]

        print("Heap desorganziada", self.heap)

        for i in range (parent(n - 1), -1, -1):
            self.binheap_siftdown(self.heap, i)

    def binheap_exchange(self, heap, i, j):

        aux = heap[i]
        self.heap[i] = heap[j]
        self.heap[j] = aux
        print(self.heap)

    def binheap_siftdown(self, heap, start):

        l = left(start)
        r = right(start)
        m = start


        if(l < self.size and cmp(heap[l], heap[m])):
            m = l
        if(r < self.size and cmp(heap[r], heap[m])):
            m = r
        if(m == start):
            print(self.heap)
            return

        self.binheap_exchange(heap, start, m)
        self.binheap_siftdown(heap, m)

    def binheap_siftup(self, heap, start):

        p = parent(start)

        if((p>=math.inf) or (p<0) or cmp(self.heap[p], self.heap[start])):
            return

        self.binheap_exchange(heap, start, p)
        self.binheap_siftup(self.heap, p)

def main():

    a = [35, 26, 33, 15, 24, 5, 4, 12, 1, 23, 21, 2]

    bh = binheap(12)
    bh.binheap_make(12, a)
    #bh.binheap_min()



main()
