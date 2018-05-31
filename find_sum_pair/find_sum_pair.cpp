#include <iostream>
#include <unordered_map>

using namespace std;

bool print_sum_pairs(int A[], int n, int sum)
{
    unordered_map<int,int> map;
    
    for (int i=0;i<n;i++){
		
		if (map.find(sum-A[i]) != map.end()){
		
		    cout << "Pair found on index ["<< map[ sum-A[i] ] << " , "<<i<<"]\n";
			return true;
		}
		map.insert( pair<int,int>(A[i],i) );
	}
	cout << "No pair with sum "<<sum <<" found\n";
    return false;
}

int main(int argc, char * argv[]){
	int ar[] = { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 };
	int n = 10;
	int sum = 7;
    cout << "Prints is value pair that sum "<<sum<<" were found\n";
    print_sum_pairs(ar,n,sum);
}
