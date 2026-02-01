const SalesEmployee = require('./salesEmployee');
var ITrainer = require('../Interfaces/ITrainer');

class salesManager extends SalesEmployee {
    constructor(id, firstname, lastname, baseSalary, hra, tax, commision, bonus) {
        super(id, firstname, lastname, baseSalary, hra, tax, commision, bonus);
        this.bonus = bonus;
    }
    computePay() {
        return super.computePay() + this.bonus;

    }
    doWork() {
        console.log("Sales Manager is working..")
    }
    conductTraining() {
        console.log("SalesManager conducting training session.");
    }
    conductHandsOnSession() {
        console.log("SalesManager conducting hands-on session.");
    }
}
module.exports = salesManager;