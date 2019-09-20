
# creating a class Car and adding properties and methods to it
class Car:    
    modelName = "Suzuki WagonR"

    def getInfo(self):
        return "The model name of this car is "+self.modelName
		
# main function 
def mainFunc():
    car = Car()
    print(car.modelName)
    print(car.getInfo())
	
mainFunc()
