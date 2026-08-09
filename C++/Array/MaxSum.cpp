#include<iostream>
#include<vector>
using namespace std;

int main(){
    int size=5;
    int arr[size]={2, -7, 15, -11, 6};
    int maxSum = 0;
    
    for (int st=0; st<=size; st++){
        int curSum = 0;
        for (int end=st; end<size; end++){ 
            curSum += arr[end];
           maxSum = max(curSum, maxSum);
            }
        }
    cout<< "The maximum sum: "<<maxSum;
    return 0;
}
//O(n^2)