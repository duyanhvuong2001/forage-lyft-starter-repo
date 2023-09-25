from car import Car
from engine import capulet_engine, sternman_engine, willoughby_engine
from battery import nubbin_battery, spindler_battery
from datetime import datetime

class CarFactory:

    @staticmethod
    def create_calliope(current_date: datetime, last_service_date: datetime, current_mileage, last_service_mileage) -> Car:
        engine = capulet_engine.CapuletEngine(last_service_mileage, current_mileage)
        battery = spindler_battery.SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        return Car(engine, battery)
    
    @staticmethod
    def create_glissade(current_date: datetime, last_service_date: datetime, current_mileage, last_service_mileage) -> Car:
        engine = willoughby_engine.WilloughbyEngine(last_service_mileage,current_mileage)
        battery = spindler_battery.SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)
    
    @staticmethod
    def create_palindrome(current_date: datetime, last_service_date: datetime, warning_light_on) -> Car:
        engine = sternman_engine.SternmanEngine(warning_light_on)
        battery = spindler_battery.SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)
    
    @staticmethod
    def create_rorschach(current_date: datetime, last_service_date: datetime, current_mileage, last_service_mileage) -> Car:
        engine = willoughby_engine.WilloughbyEngine(last_service_mileage, current_mileage)
        battery = nubbin_battery.NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)
    
    @staticmethod
    def create_thovex(current_date: datetime, last_service_date: datetime, current_mileage, last_service_mileage) -> Car:
        engine = capulet_engine.CapuletEngine(last_service_mileage, current_mileage)
        battery = nubbin_battery.NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)
