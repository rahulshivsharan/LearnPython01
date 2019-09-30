
class Car:
    manufacturer = "Suzuki" # is a class variable, shared accross all the objects

    def __init__(self,modelName):
        self.modelName = modelName
		
def mainFn():
    car01 = Car("Wagon-R")
    print(Car.manufacturer+" "+car01.modelName)
    Car.manufacturer = "Toyota"
    car02 = Car("Innova")
    print(Car.manufacturer+" "+car02.modelName)

	
mainFn()
