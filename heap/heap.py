#!/usr/bin/env python

import sys

def parent(i):
    return (i-1)/2

def left(i):
    return (2*i + 1)

def right(i):
    return (2*i + 2)


class Heap:

    def __init__(self):
        self.arr = []
        
    def swap(self, i,j):
        elem = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = elem
        
    def min_heapify(self,i):
        n = len(self.arr)
        l = left(i)
        r = right(i)
        
        smallest = i
        
        if l<n and self.arr[l] < self.arr[i]:
            smallest = l
        if r<n and self.arr[r]< self.arr[smallest]:
            smallest = r
            
        if smallest != i:
            self.swap(i,smallest)
            self.min_heapify(smallest)
            
    def insert(self,v):
        self.arr.append(v)
        
        i = len(self.arr)-1
        
        while i != 0 and self.arr[ parent(i)] > self.arr[i]:
            self.swap(i,parent(i))
            i = parent(i)
            
    def extract_min(self):
        n = len(self.arr)
        if n == 0:
            return None
            
        root = self.arr[0]
        
        self.arr[0] = self.arr[ n-1]
        
        self.min_heapify(0)
        
        self.arr.pop()
        
        return root
            
    def show(self,i=0, l=0):
        if i >= len(self.arr):
            return
        preffix = '  ' * l
        print preffix + str(self.arr[i]) + "\n"
        
        self.show(left(i), l+1)
        self.show(right(i), l+1)

            

def heap_test():
    h = Heap()

    h.insert (25)
    h.insert (20)
    h.insert (18)
    h.insert(15)
    h.insert(10)
    h.insert(8)
    h.insert(6)
    h.insert(3)
    h.insert(2)

    h.show()

    m = h.extract_min()

    print "min is "+str(m)

    h.show()


def main(argv):
    heap_test()
        
        

if __name__ == "__main__":
   main(sys.argv[1:])
