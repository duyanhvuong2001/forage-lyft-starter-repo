from engine.engine import Engine


class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileague, current_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileague

    def needs_service(self):
        return (self.current_mileage - self.last_service_mileage) > 60000
