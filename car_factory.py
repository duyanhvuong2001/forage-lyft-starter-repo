from car import Car
from engine import capulet_engine, sternman_engine, willoughby_engine
from battery import nubbin_battery, spindler_battery
from datetime import datetime
from tire import tire,carrigan_tire,octoprime_tire
class CarFactory:

    @staticmethod
    def create_calliope_with_carrigan_tire(current_date: datetime, last_service_date: datetime, current_mileage, last_service_mileage, tire_indicators) -> Car:
        engine = capulet_engine.CapuletEngine(last_service_mileage, current_mileage)
        battery = spindler_battery.SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        tire = carrigan_tire.CarriganTire(tire_indicators)
        return Car(engine, battery, tire)
    
    @staticmethod
    def create_calliope_with_octoprime_tire(current_date: datetime, last_service_date: datetime, current_mileage, last_service_mileage, tire_indicators) -> Car:
        engine = capulet_engine.CapuletEngine(last_service_mileage, current_mileage)
        battery = spindler_battery.SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        tire = octoprime_tire.OctoprimeTire(tire_indicators)
        return Car(engine, battery, tire)
    
    @staticmethod
    def create_glissade_with_carrigan_tire(current_date: datetime, last_service_date: datetime, current_mileage, last_service_mileage, tire_indicators) -> Car:
        engine = willoughby_engine.WilloughbyEngine(last_service_mileage,current_mileage)
        battery = spindler_battery.SpindlerBattery(last_service_date, current_date)
        tire = carrigan_tire.CarriganTire(tire_indicators)
        return Car(engine, battery, tire)
    
    @staticmethod
    def create_glissade_with_octoprime_tire(current_date: datetime, last_service_date: datetime, current_mileage, last_service_mileage, tire_indicators) -> Car:
        engine = willoughby_engine.WilloughbyEngine(last_service_mileage,current_mileage)
        battery = spindler_battery.SpindlerBattery(last_service_date, current_date)
        tire = octoprime_tire.OctoprimeTire(tire_indicators)
        return Car(engine, battery, tire)
    
    @staticmethod
    def create_palindrome_with_carrigan_tire(current_date: datetime, last_service_date: datetime, warning_light_on, tire_indicators) -> Car:
        engine = sternman_engine.SternmanEngine(warning_light_on)
        battery = spindler_battery.SpindlerBattery(last_service_date, current_date)
        tire = carrigan_tire.CarriganTire(tire_indicators)
        return Car(engine, battery, tire)
    
    @staticmethod
    def create_palindrome_with_octoprime_tire(current_date: datetime, last_service_date: datetime, warning_light_on, tire_indicators) -> Car:
        engine = sternman_engine.SternmanEngine(warning_light_on)
        battery = spindler_battery.SpindlerBattery(last_service_date, current_date)
        tire = octoprime_tire.OctoprimeTire(tire_indicators)
        return Car(engine, battery, tire)
    
 
    
    @staticmethod
    def create_rorschach_with_carrigan_tire(current_date: datetime, last_service_date: datetime, current_mileage, last_service_mileage,tire_indicators) -> Car:
        engine = willoughby_engine.WilloughbyEngine(last_service_mileage, current_mileage)
        battery = nubbin_battery.NubbinBattery(last_service_date, current_date)
        tire = carrigan_tire.CarriganTire(tire_indicators)
        return Car(engine, battery, tire)
    
    @staticmethod
    def create_rorschach_with_octoprime_tire(current_date: datetime, last_service_date: datetime, current_mileage, last_service_mileage,tire_indicators) -> Car:
        engine = willoughby_engine.WilloughbyEngine(last_service_mileage, current_mileage)
        battery = nubbin_battery.NubbinBattery(last_service_date, current_date)
        tire = octoprime_tire.OctoprimeTire(tire_indicators)
        return Car(engine, battery, tire)
    
    @staticmethod
    def create_thovex_with_carrigan_tire(current_date: datetime, last_service_date: datetime, current_mileage, last_service_mileage, tire_indicators) -> Car:
        engine = capulet_engine.CapuletEngine(last_service_mileage, current_mileage)
        battery = nubbin_battery.NubbinBattery(last_service_date, current_date)
        tire = carrigan_tire.CarriganTire(tire_indicators)
        return Car(engine, battery, tire)

    @staticmethod
    def create_thovex_with_octoprime_tire(current_date: datetime, last_service_date: datetime, current_mileage, last_service_mileage, tire_indicators) -> Car:
        engine = capulet_engine.CapuletEngine(last_service_mileage, current_mileage)
        battery = nubbin_battery.NubbinBattery(last_service_date, current_date)
        tire = octoprime_tire.OctoprimeTire(tire_indicators)
        return Car(engine, battery, tire)
