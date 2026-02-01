import Employee from './employee.js';
import SalesEmployee from './salesemployee.js';
import SalesManager from './salesmanager.js';
import IAppraisable from './Interfaces/IApprisable.js';
import ITrainer from './Interfaces/ITrainer.js';

var emp = new Employee(1, "John Doe", 50000, 10000, 5000);
console.log(`Employee Pay: ${emp.computePay()}`);
//emp.doWork(); //it is abstract method, will throw error
emp.computePay(); //it is virtual method, will work

var salesEmp = new SalesEmployee(2, "Jane Smith", 60000, 12000, 6000, 5000);
console.log(`Sales Employee Pay: ${salesEmp.computePay()}`);
salesEmp.doWork(); //it is overridden method, will work
salesEmp.computePay(); //it is overridden method, will work

    