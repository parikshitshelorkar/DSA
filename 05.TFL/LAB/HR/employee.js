class Employee{

    constructor(id, firstname, lastname, baseSalary, hra, tax){
        this.id = id;
        this.firstname = firstname;
        this.lastname = lastname;
        this.baseSalary = baseSalary;
        this.hra = hra;
        this.tax = tax;

    }
    computePay(){
        return this.baseSalary + this.hra - this.tax;
    }
    doWork(){
        throw new Error("Method 'doWork()' must be implemented.");
    }
}
module.exports = Employee;  