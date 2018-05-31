#!/usr/bin/env python

def naive_fib(n):
    if n<=1:
        return n
    return naive_fib(n-1) + naive_fib(n-2)
    

def fib(n, lookup):
    if n<=1:
       return n

    if (n not in lookup):
        lookup[n] = fib(n-1,lookup)+fib(n-2,lookup)
    
    return lookup[n]

l={}
x = 35



print "Hash Fibonacci of "+str(x)+ " is "+ str( fib(x, l) )+ "\n" 

print "l is "+str(l) + "\n"

print "Naive Fibonacci of "+str(x)+ " is "+ str( naive_fib(x) )+ "\n" 
