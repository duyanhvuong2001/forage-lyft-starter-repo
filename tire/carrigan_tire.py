from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, indicator_array):
        self.indicator_array = indicator_array
        
    def needs_service(self):
        for i in self.indicator_array:
            if i >= 0.9:
                return True
        
        return False