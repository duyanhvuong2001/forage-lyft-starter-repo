import unittest
from datetime import datetime
import car_factory

class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire_indicators = [0,0,0,0]
        car = car_factory.CarFactory.create_calliope_with_carrigan_tire(today, last_service_date, current_mileage, last_service_mileage, tire_indicators)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        tire_indicators = [0,0,0,0]
         
        car = car_factory.CarFactory.create_calliope_with_carrigan_tire(today, last_service_date, current_mileage, last_service_mileage, tire_indicators)

        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        tire_indicators = [0,0,0,0]
        
        
        car = car_factory.CarFactory.create_calliope_with_carrigan_tire(last_service_date, last_service_date, current_mileage, last_service_mileage, tire_indicators)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_indicators = [0,0,0,0]
        
        car = car_factory.CarFactory.create_calliope_with_octoprime_tire(last_service_date, last_service_date, current_mileage, last_service_mileage, tire_indicators)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire_indicators = [0,0,0,0]
        
        
        car = car_factory.CarFactory.create_glissade_with_octoprime_tire(today,last_service_date, current_mileage, last_service_mileage,tire_indicators)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = car_factory.CarFactory.create_glissade_with_carrigan_tire(today,last_service_date, current_mileage, last_service_mileage,tire_indicators=[0,0,0,0])
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = car_factory.CarFactory.create_glissade_with_carrigan_tire(last_service_date,last_service_date, current_mileage, last_service_mileage,tire_indicators=[0,0,0,0])
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = car_factory.CarFactory.create_glissade_with_octoprime_tire(last_service_date,last_service_date, current_mileage, last_service_mileage,tire_indicators=[0,0,0,0])
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False

        car = car_factory.CarFactory.create_palindrome_with_carrigan_tire(today, last_service_date, warning_light_is_on,tire_indicators=[0,0,0,0])
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False

        car = car_factory.CarFactory.create_palindrome_with_carrigan_tire(today, last_service_date, warning_light_is_on,tire_indicators=[0,0,0,0])
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        car = car_factory.CarFactory.create_palindrome_with_octoprime_tire(last_service_date, last_service_date, warning_light_is_on,tire_indicators=[0,0,0,0])
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False

        car = car_factory.CarFactory.create_palindrome_with_carrigan_tire(last_service_date, last_service_date, warning_light_is_on,tire_indicators=[0,0,0,0])
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = car_factory.CarFactory.create_rorschach_with_octoprime_tire(today,last_service_date, current_mileage, last_service_mileage,tire_indicators=[0,0,0,0])
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = car_factory.CarFactory.create_rorschach_with_carrigan_tire(today,last_service_date, current_mileage, last_service_mileage,tire_indicators=[0,0,0,0])
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = car_factory.CarFactory.create_rorschach_with_octoprime_tire(last_service_date,last_service_date, current_mileage, last_service_mileage,tire_indicators=[0,0,0,0])
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = car_factory.CarFactory.create_rorschach_with_octoprime_tire(last_service_date,last_service_date, current_mileage, last_service_mileage,tire_indicators=[0,0,0,0])
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = car_factory.CarFactory.create_thovex_with_octoprime_tire(today, last_service_date, current_mileage, last_service_mileage,tire_indicators=[0,0,0,0])
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = car_factory.CarFactory.create_thovex_with_octoprime_tire(today, last_service_date, current_mileage, last_service_mileage,tire_indicators=[0,0,0,0])
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = car_factory.CarFactory.create_thovex_with_octoprime_tire(last_service_date, last_service_date, current_mileage, last_service_mileage,tire_indicators=[0,0,0,0])
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = car_factory.CarFactory.create_thovex_with_carrigan_tire(last_service_date, last_service_date, current_mileage, last_service_mileage,tire_indicators=[0,0,0,0])
        self.assertFalse(car.needs_service())

class TestCarriganTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tire_indicators = [0, 0, 0.91, 0]
        car = car_factory.CarFactory.create_thovex_with_carrigan_tire(last_service_date, last_service_date, current_mileage, last_service_mileage,tire_indicators)
        self.assertTrue(car.needs_service())
        
    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tire_indicators = [0, 0, 0.89, 0.89]
        
        car = car_factory.CarFactory.create_thovex_with_carrigan_tire(last_service_date, last_service_date, current_mileage, last_service_mileage,tire_indicators)
        self.assertFalse(car.needs_service())

class TestOctoprimeTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tire_indicators = [1, 1, 1, 0]
        car = car_factory.CarFactory.create_thovex_with_octoprime_tire(last_service_date, last_service_date, current_mileage, last_service_mileage,tire_indicators)
        self.assertTrue(car.needs_service())
        
    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tire_indicators = [1, 1, 0.99, 0]
        
        car = car_factory.CarFactory.create_thovex_with_octoprime_tire(last_service_date, last_service_date, current_mileage, last_service_mileage,tire_indicators)
        self.assertFalse(car.needs_service())
if __name__ == '__main__':
    unittest.main()
