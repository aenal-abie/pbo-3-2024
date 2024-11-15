from abc import ABC, abstractmethod

# Kelas abstrak
class Vehicle(ABC):
    
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass


v = Vehicle()

# Kelas turunan yang mengimplementasikan metode abstrak
class Car(Vehicle):
    
    def start_engine(self):
        print("Starting car engine...")
    
    def stop_engine(self):
        print("Stopping car engine...")

class Bike(Vehicle):
    
    def start_engine(self):
        print("Starting bike engine...")
    
    def stop_engine(self):
        print("Stopping bike engine...")

# Instansiasi objek
car = Car()
car.start_engine()  # Output: Starting car engine...
car.stop_engine()   # Output: Stopping car engine...

bike = Bike()
bike.start_engine()  # Output: Starting bike engine...
bike.stop_engine()   # Output: Stopping bike engine...
