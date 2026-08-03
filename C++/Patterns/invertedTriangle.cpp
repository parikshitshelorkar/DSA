#include <iostream>
using namespace std;

int main(){
    int n = 4;

    for(int i=0; i<n; i++){

        for (int j=0; j<i; j++){ // i times space

            cout << " ";
            
        }
        for (int k=0; k<n-i; k++){

            cout << i+1 ;
        }
        cout << endl;
    }
    return 0;
}

