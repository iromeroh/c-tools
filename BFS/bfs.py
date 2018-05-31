#!/usr/bin/env python

class Graph:
    def __init__(self):
        self.edges = {}
        
    def addEdge(self,i,j):
        if i not in self.edges:
            self.edges[i] = [] 
        self.edges[i].append(j)
    
    def bfs(self,v):
        visited=[ False for x in self.edges]
        
        queue = []
        
        queue.append(v)
        visited[v]=True
        
        while queue:
            s = queue.pop()
            
            print "S is "+ str(s)
            
            for i in self.edges[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i]=True
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print "Following is Breadth First Traversal (starting from vertex 2)"

g.bfs(2)