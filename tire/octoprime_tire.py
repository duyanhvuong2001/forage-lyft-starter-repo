from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, indicator_array):
        self.indicator_array = indicator_array
        
    def needs_service(self):
        return sum(self.indicator_array) >= 3