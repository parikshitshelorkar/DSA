#include<iostream>
#include<vector>
#include <algorithm>

int main(){
    int size=5;
    int arr[size]={2, -7, 15, -11, 6};
    int maxSum = 0, curSum=0;

    for(int val: arr){
        curSum+=val;
        maxSum = std::max(curSum, maxSum);

        if(curSum<0){
            curSum=0;
        }
    }
    std::cout<<maxSum;
    return maxSum;
}
// O(n)...kadane's algo