#include<iostream>
using namespace std;

class Employee{

    public:
        virtual void calculateSalary(){
            cout<< "Calculating Salary of Employee.."<<endl;
        }
        virtual void work(){
            cout<<"Work of Employee"<<endl;
        }
};

class SalesEmployee : public Employee{

    public:
    void calculateSalary() override{
        cout<<"Calculating salary of Sales Employee.."<<endl;

    }
};

//concept of virtual
//vptr and vtable
int main(){
    Employee* emp; //object and pointer of employee
    emp = new SalesEmployee();
    emp->calculateSalary();
    return 0;
}

//jevha class maddhye virtual keyword yeto tyasathi vtable tayar hoto
//