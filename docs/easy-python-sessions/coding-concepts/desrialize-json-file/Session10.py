import json
import os

class car:

    total_distance_travelled = 0

    def __init__(self,_brand:str,_model,_color,_fuel_in_liters:int):
        self.brand = _brand
        self.model = _model
        self.color = _color
        self.fuel_in_liters = _fuel_in_liters
        self.NoOfWheels = 4
        self.trips = []

    
    @classmethod
    def import_from_json(cls, file_path):
        try: 
            json_data = open(file_path,'r')
            json_obj = json.load(json_data)

            return cls(
                _brand = json_obj["brand"],
                _model = json_obj["model"],
                _color = json_obj["color"],
                _fuel_in_liters = json_obj["fuel_in_liters"]
            )
        except FileNotFoundError:
            print(f"File not found in location: {file_path}")
        except json.JSONDecodeError:
            print(f"Error processing json: {file_path}")

    def display_brand(self):
        print(f"The brand of the car is : {self.brand}")


    def record_a_trip(self,destination:str,distance_one_way:int,fuel_needed_in_liters:int):
        if fuel_needed_in_liters >= self.fuel_in_liters:
            print("Not enough fuel")
        else:
            self.total_distance_travelled += distance_one_way*2
            self.fuel_in_liters -= fuel_needed_in_liters
            print(f"Trip to {destination} was awesome, its was {distance_one_way} kms far way, and needed {fuel_needed_in_liters} liters of pertol")
            self.trips.append(f"Trip to {destination} was awesome, its was {distance_one_way} kms far way, and needed {fuel_needed_in_liters} liters of pertol.")

    def check_fuel(self):
        print(f"current fuel level is : {self.fuel_in_liters}, total distance travelled : {self.total_distance_travelled}")

    def trips_report(self):
        print(self.trips)

folder_path = os.path.dirname(__file__)
json_path = os.path.join(folder_path,"my_car.json")

myNextCar = car.import_from_json(json_path)
myNextCar.display_brand()
myNextCar.record_a_trip("Montreal",20,20)
myNextCar.record_a_trip("Hamilton falls",30,30)
myNextCar.trips_report()
myNextCar.check_fuel()

car.display_brand()

# mycar = car("Acura","MDX","Grey",200)
# mycar.check_fuel()
# mycar.display_brand()
# mycar.record_a_trip("Montreal",20,20)
# mycar.check_fuel()
# mycar.record_a_trip("Hamilton falls",30,30)
# mycar.trips_report()
# mycar.check_fuel()


# myNewCar = car("Kia","sorento","black",90)
# myNewCar.check_fuel()
# myNewCar.display_brand()
# myNewCar.record_a_trip("Gelph",5,50)
# myNewCar.check_fuel()
# myNewCar.record_a_trip("Kitchner falls",10,30)
# myNewCar.trips_report()
# myNewCar.check_fuel()

# MyThirdCar = car(_fuel_in_liters = 10,_model="Seinna",_brand="Tayota",_color="white")
# MyThirdCar.record_a_trip()