const Employee = require("./employee");

class SalesEmployee extends Employee{
    constructor(id, firstname, lastname, baseSalary, hra, tax, commission){
        super(id, firstname, lastname, baseSalary, hra, tax)
        this.bonus = commission;

    }
    computePay(){
        return this.baseSalary + this.hra - this.tax + this.bonus;
    }
    doWork(){
        console.log("Sales Employee is working..!");
    }

}
module.exports = SalesEmployee;