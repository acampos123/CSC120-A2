class Computer:
    #class representing one computer within a resale shop

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
    def update_price(self: dict, new_price: int):
        #replaces current price of a computer witj a new integer
        self.price = new_price
        return self.price

    def update_os(self: dict, new_opsys: str):
        #replaces current operating system of a computer with a new string
        self.operating_system = new_opsys
        return self.operating_system
        
def main():
   myComputer:Computer = Computer("2019 MacBook Pro","Intel", 256, 16, "Sequoia", 2019, 1000)
   otherComputer:Computer = Computer("2000 MacBook Air", "Intel", 256, 16, "High Sierra", 2010, 500)
   print(myComputer.update_price(200))
   print(otherComputer.update_os("High OS"))


if __name__ == "__main__":
    main()   