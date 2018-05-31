#include <iostream>
#include <unordered_map>

using namespace std;

void print_zero_sum_subarrays(int A[], int n)
{
    unordered_multimap<int,int> map;
    
    map.insert( pair<int,int>(0,-1) );
    
    int sum = 0;
    
    for (int i=0;i<n;i++){
		sum += A[i];
		
		if (map.find(sum) != map.end()){
			
			auto it = map.find(sum);
			
			while (it != map.end() && it->first == sum){
				cout << "Sub-array [ "<< it->second+1 << " .. "<< i << "]\n";
				it++;
			}
		}
		map.insert( pair<int,int>(sum,i) );
	}

}

int main(int argc, char * argv[]){
	int ar[] = { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 };
	int n = 10;
    cout << "Prints all zero sum subarrays of an array of integers\n";
    print_zero_sum_subarrays(ar,n);
}
