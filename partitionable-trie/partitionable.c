#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ALPHABET_SIZE  26

typedef struct Node {
    unsigned int defined;
    
    struct Node * next[ALPHABET_SIZE];
} Trie;

Trie * make_node()
{
    Trie * node = (Trie *) malloc(sizeof(Trie));
    
    if (!node)
        return NULL;
    
    node->defined = 0;
    
    for (int i=0; i<ALPHABET_SIZE; i++)
        node->next[i] = NULL;

    return node;
}

int insert(Trie * root, char* str)
{
    int len = strlen(str);
    Trie * current = root;
    
    for (int i =0; i<len; i++){
        if (!current->next[ str[i] - 'a' ]){
            Trie * node = make_node();
            if (!node)
                return 0;
            current->next[ str[i] - 'a' ] = node;
        }
        current = current->next[ str[i] - 'a' ];
    }
    current->defined = 1;
    return 1; 
}

int find (Trie * root, char *str){
    int len = strlen(str);
    Trie * current = root;
    
    for (int i =0; i<len; i++){
        if (!current->next[ str[i] - 'a' ]){
            return 0;
        }
        current = current->next[ str[i] - 'a' ];
    }
    return current->defined;
}

void delete_trie(Trie * root){
    if (!root)
        return;
    for (int i=0; i< ALPHABET_SIZE; i++){
        delete_trie(root->next[i]);
    }
    free(root);
}

void insert_dict(Trie * root, char* dict[], int n)
{
    for (int i=0; i< n ; i++){
        insert (root, dict[i]);
    }
}

int partitionable(Trie * root, char * str){
    int len = strlen(str);
    
    char * good = (char *) malloc(len+1);
    
    memset(good,0x00, len);
    good[0] = 1;
    
    for (int i =0; i< len; i++){
        if (good[i]){
            Trie * curr = root;
            for (int j=i;j<len;j++){
                if (!curr)
                    break;
                curr = curr->next[ str[j] - 'a'];
                
                if (curr && curr->defined)
                    good[j+1] = 1;
            }
        }
        
    }
    return good[len];
}

char * dict[] = {
    "anita",
    "lava",
    "la",
    "tina",
    "con",
    "un",
    "trapo",
    "y",
    "jabon"
};

int main(int argc, char * argv){

    Trie * t = make_node();
    
    char * s = "conuntrapoyjabonanitalava";
    
    insert_dict(t,dict,9);
    
    if ( partitionable (t,s) )
        printf("String %s is partitionable into words of the dictionary\n", s);
    else
        printf("String %s is NOT partitionable using words of the dictionary\n", s);   
}