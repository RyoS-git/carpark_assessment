
from display import Display
from car_park import CarPark
# ... inside the TestDisplay class
def test_display_initialized_with_all_attributes(self):
   self.assertIsInstance(self.display, Display)
   self.assertEqual(self.display.id, 1)
   self.assertEqual(self.display.message, "Welcome to the car park")
   self.assertEqual(self.display.is_on, True)

   # ... inside the TestDisplay class
   def test_update(self):
       self.display.update({"message": "Goodbye"})
       self.assertEqual(self.display.message, "Goodbye")
