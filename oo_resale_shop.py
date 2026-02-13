from computer import *

class ResaleShop:
    #class represnting a store that performs functions with multiple computers

    # What attributes will it need?
    inventory:list = []

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory: list):
        self.inventory = inventory

    # What methods will you need?
    def buy(self, Computer):
       #adds a new computer to the inventory
       self.inventory.append(Computer)
       return self.inventory
        
    def sell(self, Computer):
      #removes a computer from the inventory
      if Computer in self.inventory:
        self.inventory.remove(Computer)
        return self.inventory
      else: 
         print("Computer not found. Please select another item to sell.")
       
    def print_inventory(self):
       #prints the inventory with appended/removed computers
       print(self.inventory)

    def update_price(self, Computer, new_price:int):
        if Computer in self.inventory:
           Computer.update_price(new_price)
           print (new_price)
        else:
            print("Computer not found. Cannot update price.")
           
   

    def refurbish(self, Computer, new_os: str = None): 
        #updates price and/or operating system depending on year made and operating system status
        if Computer in self.inventory:
            if int(Computer.year_made) < 2000:
                Computer.price = 0 # too old to sell, donation only
            elif int(Computer.year_made) < 2012:
                Computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(Computer.year_made) < 2018:
                Computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                Computer.price = 1000 # recent stuff

            if new_os is not None:
                Computer.operating_system = new_os # update details after installing new OS
        else:
            print("Computer not found. Please select another item to refurbish.")

def main():
   print (ResaleShop.inventory)
   resaleShop = ResaleShop([])
   myComputer:Computer = Computer("2019 MacBook Pro","Intel", 256, 16, "Sequoia", 2019, 1000)
   otherComputer:Computer = Computer("2000 MacBook Air", "Intel", 256, 16, "High Sierra", 2010, 500)
   print(resaleShop.buy(myComputer))
   print(resaleShop.buy(otherComputer))
   resaleShop.print_inventory()
   resaleShop.update_price(myComputer, 200)
   print(otherComputer.update_os("High OS"))
   print(resaleShop.inventory)


if __name__ == "__main__":
    main()

        
   
        