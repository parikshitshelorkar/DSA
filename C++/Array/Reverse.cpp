#include <iostream>
using namespace std;
//Two pointer approach
void reverseArray(int arr[], int sz)
{
    int start = 0;
    int end = sz - 1;
    
    while (start < end)
    {
        swap(arr[start], arr[end]);
        start++;
        end--;
    }
}
int main()
{
    int arr[] = {1, 3, 5, 7, 9, 6, 2};
    int sz = 7;
    int i=0;

    reverseArray(arr,sz);

    for(i=0; i<sz; i++){
        cout<< arr[i] <<" ";
    }

    return 0;
}
//Time complexity: O(n)