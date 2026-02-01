//Constructor copy/clone
#include<stdio.h>
using namespace std;
class Patient {
public:
    int id;
    Patient(int id) : id(id) {}
    Patient(const Patient& p) : id(p.id) {}
};
