from oo_resale_shop import *

class Computer:

    # What attributes will it need?
    description: str = ""
    processor_type: str = ""
    hard_drive_capacity: int = 0
    memory: int = 0
    operating_system: str= ""
    year_made: int = 0
    price: int = 0

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description:str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str,
                 year_made: int, price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
        

    # What methods will you need?
    def update_price(self: Dict, new_price: int):
        if self in inventory:
            self.price = new_price
        else:
            return("Computer not found. Cannot update price.")

    def new_os():
        pass
        
    def refurbish(self: Dict, new_os: Optional[str] = None):
        if self in inventory:
            if int(self.year_made) < 2000:
                self.price = 0 # too old to sell, donation only
            elif int(self.year_made) < 2012:
                self.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(self.year_made) < 2018:
                self.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                self.price = 1000 # recent stuff

            if new_os is not None:
                self.operating_system = new_os # update details after installing new OS
        else:
            print("Computer not found. Please select another item to refurbish.")