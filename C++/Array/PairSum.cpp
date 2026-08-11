#include <iostream>
using namespace std;
//Finding the pair for required sum

int main()
{   //sorted array
    int n = 4;
    int arr[] = {2, 7, 11, 15};
    int i = 0, j = n-1, pairSum;
    int target = 26;

    while (i<j)
    {
        pairSum= arr[i]+arr[j];
        if (pairSum<target)
        {
            i++;
        }
        else if(pairSum>target){
            j--;
        }
        else{
            cout << "Pair found!" << endl;
            cout << "Indices: " << i << " and " << j << endl;
            return i,j, pairSum;
        }   
        
        
    }
    
    return 0;
}
//Time Complexity: O(n)
