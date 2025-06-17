from sensor import Sensor
from display import Display

class CarPark:
    def __init__(self, location: str, capacity: int, plate=None, displays=None):
        self.location = location
        self.displays = displays or []
        self.capacity = capacity
        self.plate = plate or []

    def __str__(self):
       return "Car park at " + (self.location) + " ,with" + (self.capacity) + " bays"
        # When you print a CarPark object, this method will be called.
        # The method should return a string containing the car park's location and capacity.
        # For example, "Car park at 123 Example Street, with 100 bays.".

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)
            # TODO: (optional) add an elif to check if the component is a Display - MUST

    def add_car(self, plate):
            self.plate.append(plate)
            self.update_displays()

    def remove_car(self, plate):
        if plate in self.plate:
            self.plate.remove(plate)
        self.update_displays()

    def register(self,component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def update_displays(self):
        message = f"{self.available_bays} spaces available"
        data = {"^available_bays": self.available_bays,
                "temperature": 25}
        for display in self.displays:
            display.update(message)


    @property
    def available_bays(self):
        return self.capacity - len(self.plates)

    def update(self, data):
        print(f"Display {self.id} status")
        for key, value in data.items():
            print(f"{key}: {value}")