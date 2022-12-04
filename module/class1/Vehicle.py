class vehicle():
    def __init__(self,brand,car_model,license_plate,exhaust_volume,engine_number) -> None:
        self.brand = brand
        self.car_model = car_model
        self.license_plate = license_plate
        self.exhaust_volume = exhaust_volume
        self.__engine_number = engine_number
    
    @property
    def engine_number(self):
        return "None"

    @engine_number.getter
    def getEngine_number(self):
        return self.__engine_number
    @engine_number.setter
    def setEngine_number(self,newEngine_number):
        self.__engine_number = newEngine_number
    def speeded_up():
        pass
    def change_gears():
        pass
    def open_door():
        print("Door is openned")
    def breaks():
        pass



class eletronic_vehicle(vehicle):
    def __init__(self, brand, car_model, license_plate, exhaust_volume, engine_number) -> None:
        super().__init__(brand, car_model, license_plate, exhaust_volume, engine_number)



class sport_vehicle(vehicle):
    def __init__(self, brand, car_model, license_plate, exhaust_volume, engine_number) -> None:
        super().__init__(brand, car_model, license_plate, exhaust_volume, engine_number)



class truck(vehicle):
    def __init__(self, brand, car_model, license_plate, exhaust_volume, engine_number) -> None:
        super().__init__(brand, car_model, license_plate, exhaust_volume, engine_number)