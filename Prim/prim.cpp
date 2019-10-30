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
        bool add_edge_letter(char, char, int);
        void prim ();
        
        void print_matrix();
        
        void print_graph();
	void print_graph_letter();
        
        void print_MST();
	void print_MST_letter();

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

bool Graph::add_edge_letter(char i, char j, int weight){
     
     i = i - 65;
     j = j - 65;

     if (i<0 || j<0 || i>=V || j>=V )
         return false;
     
     matrix[(i*V+j)] = weight;
     matrix[(j*V+i)] = weight;
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
        cerr << "| ";
        for(int j=0;j<V;j++){
 
                cerr << matrix[i*V+j] << " ";
        }
        cerr << " |\n";
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


void Graph::print_graph_letter(){
    fprintf(stdout, "graph{\n");
    fprintf(stderr, "graph{\n");
    char i_str[2]="";
    char j_str[2]=""; 
    
    for( int i=0;i<V; i++){
        for(int j=i;j<V;j++){
            if ( matrix[i*V+j] > 0 ){
		i_str[0]=(char)i+65;
                i_str[1]=0x00;
		j_str[0]=(char)j+65;
                j_str[1]=0x00; 
                fprintf(stdout,"  %s -- %s [label=\"%d\"];\n",i_str,j_str,matrix[i*V+j]);
		fprintf(stderr,"  %s -- %s [label=\"%d\"];\n",i_str,j_str,matrix[i*V+j]);
             }
        }
    }
    fprintf(stdout, "}\n");
    fprintf(stderr, "}\n");
}

void Graph::print_MST(){
    cout << "graph{\n";
    
    for (int i=1;i<V;i++){
            cout << "    "<<parent[i]<<" -- "<< i << " [label=\""<< matrix[ (parent[i]*V)+i] << "\"];\n";
    } 
    cout << "}\n";
}

void Graph::print_MST_letter(){
    cout << "graph{\n";
    cerr << "graph{\n";
    char p_i_str[2]="";
    char i_str[2]="";

    for (int i=1;i<V;i++){
            p_i_str[0] = (char)(parent[i]+65);
            i_str[0]=char(i+65);
            cout << "    "<< p_i_str<<" -- "<< i_str << " [label=\""<< matrix[ (parent[i]*V)+i] << "\"];\n";
            cerr << "    "<< p_i_str<<" -- "<< i_str << " [label=\""<< matrix[ (parent[i]*V)+i] << "\"];\n";
    } 
    cout << "}\n";
    cerr << "}\n";
}

int main(int argc, char*argv[]){
    Graph g(7);
    
    g.add_edge_letter('A','B',7);
    g.add_edge_letter('B','C',9);
    g.add_edge_letter('C','D',10);
    g.add_edge_letter('A','C',11);
    g.add_edge_letter('C','E',9);
    g.add_edge_letter('D','E',7);
    g.add_edge_letter('A','G',8);
    g.add_edge_letter('E','G',8);
    g.add_edge_letter('G','F',13);
    g.add_edge_letter('E','F',11);

    if (argc>1){
       if(strcmp(argv[1],"show")==0){
         g.print_graph_letter();
       }
       if(strcmp(argv[1],"prim")==0){
         g.prim();
         g.print_MST_letter();
       }
       
       if(strcmp(argv[1],"matrix")==0){
         g.print_matrix();
       }
       if(strcmp(argv[1],"s")==0){
         g.print_graph();
       }
       if(strcmp(argv[1],"p")==0){
         g.prim();
         g.print_MST();
       }              
    
    }
    
}


