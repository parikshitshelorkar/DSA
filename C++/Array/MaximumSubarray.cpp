#include<iostream>
using namespace std;

int main(){
    int size=5;
    int arr[size]={2,3,5,6,4};
    
    for (int st=0; st<=size; st++){//starting from index 0 to size of array
        
        for (int end=st; end<size; end++){ 
            //after each iteration the end is shifted to right
            for (int i=st; i<=end; i++){
                //possible arrays in between st and end pointers
                cout<<arr[i];
            }
            cout<<" ";
        }
        cout<<endl;
    }
    return 0;
}
