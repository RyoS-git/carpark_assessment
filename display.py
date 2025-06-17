class Display:
    def __init__(self, id, message="Welcome to the car park", is_on=False):
        self.id = id
        self.message = message
        self.is_on = is_on

    def update(self, message):
        self.message = message
        if self.is_on:
            print (f"Display {self.id} : {self.message}")
        else:
            print(f"display {self.id} is off. Cannot update message")



    def __str__(self):
        return f"{self.id}:{self.message}"
        # This method will be called when you print a Display object.
        # The method should return a string containing the display's ID and message.
        # For example, "Display 1: Welcome to the car park.".