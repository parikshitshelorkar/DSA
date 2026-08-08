#include<iostream>
using namespace std;

int const s=9;
int arr[s]={12, 23, 4,5,17,33, 2, 11};
int sum=0;

int main(){
    for(int i=0; i<s; i++){
        sum +=arr[i];
    }
    cout<<"The sum of all elements: "<<sum;

}
