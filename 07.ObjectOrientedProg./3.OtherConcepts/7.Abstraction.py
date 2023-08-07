from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def operate(self):
        pass

    def stop(self):
        print("Vehicle stopped")

class Car(Vehicle):
    def operate(self):
        print("Car started")
        print("Fuel level: 70%")
        self.stop()

class Bike(Vehicle):
    def operate(self):
        print("Bike started")
        print("No fuel, runs on passion")
        self.stop()

# Usage
car = Car()
car.operate()

bike = Bike()
bike.operate()