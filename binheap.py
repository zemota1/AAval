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
    if (a == b):
        print ('VERRRRR')

class binheap:


    def __init__(self, key, n):
        self.max_size = n
        self.size = 0
        self.heap = [None]*n
        self.key = key
        #self.map = [None]*n


    def binheap_empty(self):
        if(self.size == 0):
            return True

        return False

    def binheap_top(self):
        return self.heap[0]

    def binheap_insert(self, id):
        if(self.size >= self.max_size):
            return

        self.heap[self.size] = id
        self.size += 1

        self.binheap_siftup(self.heap)

    def binheap_min(self):

        aux = self.heap[0]
        self.size -=1

        self.binheap_exchange(self.heap, self.size, 0)
        self.binheap_siftdown(self.heap, 0)

        self.heap[self.size] = math.inf
        
        return aux

    def binheap_make(self, n):
        self.size = n

        for i in range (n):
            self.heap[i] = i

        for i in range (parent(n - 1), 0, -1):
            self.binheap_siftdown(self.heap, i)

    def binheap_exchange(self, heap, i, j):

        aux = heap[i]
        heap[i] = heap [j]
        heap[j] = aux

    def binheap_siftdown(self, heap, start):

        l = left(start)
        r = right(start)
        m = start

        if(l < self.size and cmp(heap[l], heap[m])):
            m = l
        if(r < self.size and cmp(heap[r], heap[m])):
             m = r
        if(m == start):
            return

        self.binheap_exchange(heap, start, m)
        self.binheap_siftdown(heap, m)

    def binheap_siftup(self, heap, start):
        
        p = parent(start)
        
        if(p>=math.inf or cmp(heap[p], heap[start])):
            return
        
        self.binheap_exchange(heap, start, p)
        self.binheap_siftup(heap, p)

def main():
    
    a = [2, 1, 3, 4, 0]
    
    

main()

        

    