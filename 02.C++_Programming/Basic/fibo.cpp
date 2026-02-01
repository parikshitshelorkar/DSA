#include<iostream>
#include<conio.h>
using namespace std;
int main ()
{
 
 int f0, f1, f, n, i ;
 f0 = 0;
 f1 = 1;
 cout << "Enter the size of Fibonacci: ";
 cin >> n;
 cout << "Fibonnaci Series:" << endl;
 cout << f0 << endl;
 cout << f1 << endl;
    for  (i=2 ; i < n; i++)
        { 
            f = f0 + f1;
            cout << f << endl ;
            f0 = f1;
            f1 = f;
        }
return 0;
}