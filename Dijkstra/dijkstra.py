#!/usr/bin/env python

import sys 


class Graph:

    def __init__(self, V):
        self.V = V
        self.matrix=[ [0 for i in xrange(V)] for j in xrange(V)]
    
    def set_matrix(m):
        self.matrix=m;
        
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
                    
    def print_dist(self):
        print "Node\tdistance:\n"
        
        for i in xrange(self.V):
            print i,"\t",self.dist[i]
        

g = Graph(9)

g.matrix = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
          ]
 
g.dijkstra(0)

g.print_dist()

