
class ITrainer{
    conductingTraining(){
        throw new Error("Method 'conductingTraining()' must be implemented.");
    }   
    conductHandsOnSession(){
        throw new Error("Method 'conductHandsOnSession()' must be implemented.");
    }   
}
module.exports = ITrainer;
