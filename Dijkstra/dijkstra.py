#!/usr/bin/env python

import sys

def perror(s):
	sys.stderr.write(s+'\n')

def label(i):
	if i==0:
		return 'inicio'
	else:
		return 'A'+str(i-1)

class Graph:

    def __init__(self, V):
        self.V = V
        self.matrix=[ [0 for i in xrange(V)] for j in xrange(V)]
    
    def set_matrix(self, m):
        self.matrix=m;
        
    def dot(self, to_label):
    	print ('digraph {')
    	for i in range(0,self.V):
    		print('    '+to_label(i)+';')
    	for i in range(0,self.V):
    		for j in range(0,self.V):
    			if self.matrix[i][j] != 0:
    				print('    '+to_label(i)+'->'+to_label(j)+'[label="'+str(self.matrix[i][j])+'"];')
    	print('}')
        
    def min_distance(self, dist, sptSet):
        mindist = sys.maxint
        mindex = 0
        
        for i in xrange(self.V):
            if sptSet[i]==False and dist[i]<mindist:
                mindist = dist[i]
                mindex = i
        return mindex
        
   
        
    def dijkstra(self, src):
        self.parent=[-1 for z in xrange(self.V)]
        self.dist = [sys.maxint for x in xrange(self.V)]
        sptSet = [False for y in xrange(self.V)]       
        self.dist[src] = 0
        
        for count in xrange(self.V):
            u = self.min_distance(self.dist,sptSet)
            
            sptSet[u] = True
            
            for v in xrange(self.V):
                if self.matrix[u][v]>0 and sptSet[v] == False and self.dist[v] > self.dist[u]+ self.matrix[u][v]:
                    self.dist[v] = self.dist[u]+ self.matrix[u][v]
                    
    def print_dist(self, to_label):
        perror( "Node\tdistance:")
        
        for i in xrange(self.V):
            perror( to_label(i)+"\t"+str(self.dist[i]))
        

g = Graph(11)

g.matrix = [[0,3, 0, 0, 0, 0, 0, 0, 0, 0,0],  # inicio
           [0, 0, 2, 4, 2, 2, 0, 0, 0, 0,0],  # A0
           [0, 0, 0, 4, 2, 2, 5, 0, 0, 0,0],   # A1
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],   # A2
           [0, 0, 0, 0, 0, 0, 5, 0, 0, 0,0],  # A3
           [0, 0, 0, 0, 0, 0, 5, 0, 0, 0,0], # A4
           [0, 0, 0, 0, 0, 0, 0, 2, 4, 0,0],   # A5
           [0, 0, 0, 0, 0, 0, 0, 0, 4, 2,0],  # A6
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],   # A7
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,2],  # A8
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],  # A9
          ]
g.dot(label)
 
g.dijkstra(0)

g.print_dist(label)

