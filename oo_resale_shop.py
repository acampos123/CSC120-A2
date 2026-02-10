from computer import *

class ResaleShop:

    # What attributes will it need?
    inventory = []

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory: list):
     self.inventory = inventory

    # What methods will you need?
    def buy(self):
       self.inventory.append(Computer)
        
    def sell(self):
       if Computer in inventory:
        self.inventory.remove(computer)
        else: 
        return("Computer not found. Please select another item to sell.")
        
   
        