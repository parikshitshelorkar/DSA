#include <iostream>
using namespace std;
int n = 10;
int main(){
    //For the upper part
    for (int i=0; i<n; i++){
        //triangle 1
        for (int j=0; j<i+1; j++){
            cout << "*";
    }
     for (int j=0; j<2*(n-i-1); j++){
            cout << " ";
    }
    //triangle 2
    cout << "*";
    if (i!=0){
        for (int j=0; j<i; j++){
            cout << "*";
    }
    }
    cout << endl;
}
// For the lower part
    for (int i=0; i<n; i++){
        //triangle 3
        for (int j=n; j>i; j--){
            cout << "*";
    }
    for (int j=0; j<2*(i); j++){
            cout << " ";
    }
    //triangle 4
    for (int j=n; j>i; j--){
            cout << "*";
    }
    cout << endl;
}

}