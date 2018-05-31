#include <iostream>
#include <list>
#include <malloc.h>
#include <string.h>

#define MAX_INT 100000000

using namespace std;

class Graph {

    protected:

    int V;
    
    int  * matrix;
    
    int * parent;

    public:
        Graph(int);
        
        
        int min_key ( int *, int * );
        
        void set_matrix(int *);
        
        bool add_edge(int, int, int);
        
        void prim ();
        
        void print_matrix();
        
        void print_graph();
        
        void print_MST();

};

Graph::Graph(int V)
{
    this->V = V;
    
    matrix = (int *) malloc (sizeof(int)*V*V);
    
    memset ((void *)matrix,0x00,sizeof(int)*V*V);
    
    parent = (int *) malloc (sizeof(int)*V);
    
    memset((void *)parent, 0x00, sizeof(int)*V);
    
}


void Graph::set_matrix(int * src)
{
    memcpy((void *)matrix, (void *)src, sizeof(int)*V*V); 
}

bool Graph::add_edge(int i, int j, int weight){
     
     if (i<0 || j<0 || i>=V || j>=V )
         return false;
     
     matrix[i*V+j] = weight;
     matrix[j*V+i] = weight;
     return true;
}

int Graph::min_key(int * keys, int * mtset)
{
  int min = MAX_INT;
  int min_index;
  
  for (int v=0; v<V;v++){
      if ( mtset[v] == 0 && keys[v]< min){
          min = keys[v];
          min_index = v;
      }
  }
  return min_index;
}

void print_arr(int *arr, int s){
    cout << "[ ";
    for (int i=0;i<s;i++)
        cout << arr[i] << " , ";
    cout << "]\n";
        
}

void Graph::prim ()
{
    int key [V];
    int mtset [V];
    
    for (int i=0;i<V; i++){
        key[i] = MAX_INT;
        mtset[i] = 0;
    }
    
    key[0] = 0;
    parent[0] = -1;
    
    for (int count=0; count< V-1; count++){
        
        int u = min_key((int *)key, (int *)mtset);
                
        mtset[u] = 1;
                
        for (int v=0; v<V; v++){
            if ( matrix[u*V+v] && mtset[v] == 0 && matrix[u*V+v] < key[v]){
                parent[v] = u;
                key[v] = matrix[u*V+v];
            }
                
        }
    }
        
}

void Graph::print_matrix(){
    for( int i=0;i<V; i++){
        cout << "| ";
        for(int j=0;j<V;j++){
 
                cout << matrix[i*V+j] << " ";
        }
        cout << " |\n";
    }    
}

void Graph::print_graph(){
    cout << "graph{\n";
    
    for( int i=0;i<V; i++){
        for(int j=i;j<V;j++){
            if ( matrix[i*V+j] )
                cout << "    "<< i << " -- " << j << " [label=\""<< matrix[i*V+j] << "\"]\n";
        }
    }
    cout << "}\n";
}

void Graph::print_MST(){
    cout << "graph{\n";
    
    for (int i=1;i<V;i++){
            cout << "    "<<parent[i]<<" -- "<< i << " [label=\""<< matrix[ (parent[i]*V)+i] << "\"]\n";
    } 
    cout << "}\n";
}

int main(int argc, char*argv[]){
    Graph g(9);
    
   int graph[9][9] = {{0, 4, 0, 0,  0, 0, 0, 8, 0},
                      {4, 0, 8, 0,  0, 0, 0, 11, 0},
                      {0, 8, 0, 7,  0, 4, 0, 0, 2},
                      {0, 0, 7, 0,  9, 14, 0, 0, 0},
                      {0, 0, 0, 9,  0, 10, 0, 0, 0},
                      {0, 0, 4, 14, 10, 0, 2, 0, 0},
                      {0, 0, 0, 0,  0, 2, 0, 1, 6},
                      {8, 11, 0, 0, 0, 0, 1, 0, 7},
                      {0, 0, 2, 0,  0, 0, 6, 7, 0}
                     };
    g.set_matrix((int *)graph);
        
    
    g.print_graph();
    
    g.prim();
    
    g.print_MST();
}

