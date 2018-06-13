#!/usr/bin/env python

import sys

def parent(i):
    return (i-1)/2

def left(i):
    return (2*i + 1)

def right(i):
    return (2*i + 2)
    
class Item:
    def __init__(self, char, freq, left = None, right = None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
        
    def lt(self,other):
        return self.freq < other.freq
    
    def gt(self,other):
        return self.freq > other.freq
        
    def show(self,level=0):
        preffix = '  ' * level
        print preffix + " ( '"+str(self.char) + "' , "+ str(self.freq) +" )\n"
        
        if (self.left is not None):
            self.left.show(level+1)
        if (self.right is not None):
            self.right.show(level+1)

    def bin_encode(self, lookup, string = ""):
        if self.left is None and self.right is None:
            lookup[self.char] = string
            return
        
        if self.left is not None:
            self.left.bin_encode(lookup, string+"0")
        if self.right is not None:
            self.right.bin_encode(lookup, string+"1")


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

class CharHeap (Heap):

    def min_heapify(self,i):
        n = len(self.arr)
        l = left(i)
        r = right(i)
        
        smallest = i
        
        if l<n and self.arr[l].lt (self.arr[i]):
            smallest = l
        if r<n and self.arr[r].lt( self.arr[smallest]):
            smallest = r
            
        if smallest != i:
            self.swap(i,smallest)
            self.min_heapify(smallest)
            
    def insert(self,v):
        self.arr.append(v)
        
        i = len(self.arr)-1
        
        while i != 0 and self.arr[ parent(i)].gt( self.arr[i]):
            self.swap(i,parent(i))
            i = parent(i)

    def show(self,i=0, l=0):
        if i >= len(self.arr):
            return
        preffix = '  ' * l
        print preffix + " ( '"+str(self.arr[i].char) + "' , "+ str(self.arr[i].freq) +" )\n"
        
        self.show(left(i), l+1)
        self.show(right(i), l+1)

class Huffman:

    def __init__(self):
        self.frequency = {}
        self.heap = CharHeap()
        self.dictionary = {}
        self.enc = None
        self.file = ""
        self.bits = 0


    def count_freq(self,file):
        self.file = file;
        with open(self.file, "rb") as f:
            byte = f.read(1)
            # first we extract the frequency of every byte in the file
            while byte != "":
                # Do stuff with byte.
                if byte not in self.frequency:
                    self.frequency[byte] = 1
                else:
                    self.frequency[byte] = self.frequency[byte]+1
                self.bits = self.bits + 8
                byte = f.read(1)
        for char, freq in self.frequency.items():
            ch = Item(char,freq)
            
            self.heap.insert(ch)
        
        return self.heap
        
    def make_encoding(self):
        
        while len(self.heap.arr)>1:

            r = self.heap.extract_min()
            l = self.heap.extract_min()
            
            n = Item('@',l.freq + r.freq, l, r)
            
            self.heap.insert(n)

        self.enc = self.heap.extract_min()

        return self.enc
        
    def make_dictionary(self):
        
        if self.enc is None:
            return False
        
        self.enc.bin_encode(self.dictionary)
        
        return True

    def encode_str(self, s):
        enc = ""
        for byte in s:
            enc = enc + self.dictionary[byte]
        return enc
    
    def encode_file(self):
        enc = ""
        with open(self.file, "rb") as f:
            byte = f.read(1)
            # first we extract the frequency of every byte in the file
            while byte != "":
                # Do stuff with byte.
                enc = enc + self.dictionary[byte]
                byte = f.read(1)
        return enc
        
    def decode_str(self, s):
        dec = ""
        
        curr = self.enc
                
        for bit in s:
            if bit == "0":
                curr = curr.left
            else:
                curr = curr.right
            
            if curr.left is None and curr.right is None:
                dec = dec + curr.char
                curr = self.enc                
                continue
            
        return dec


def main(argv):
    
    if len(argv) == 0:
        print "No argument provided. Call python heap.py <filename>"
        exit(1)
    huff_obj = Huffman()
    
    h = huff_obj.count_freq(argv[0])
    print "Priority queue is : "
    h.show()
    
    e = huff_obj.make_encoding()
    print "Encoding tree is : "    
    e.show()
    
    if huff_obj.make_dictionary():
        print "Dictionary is: "
        print str(huff_obj.dictionary)
        
        e = huff_obj.encode_file()
        
        print "Encoding has "+ str(len(e)) + " bits, it is: "
        #print e
        
        print "Original file has "+str(huff_obj.bits)+" bits, for a compression ratio of "+str( len(e)*100/ huff_obj.bits )+" %"
        
        d = huff_obj.decode_str(e)
        
        print "Decoded string is: " + d
        
        
        

if __name__ == "__main__":
   main(sys.argv[1:])
