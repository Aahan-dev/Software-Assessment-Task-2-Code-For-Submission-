import time
import colorama
from colorama import Fore

colorama.init()

# Prompt the user for their decision
decision = input("Welcome to Aahan's Restaurant! Would you like to order something? ").lower()

# Validate the decision input
if decision not in ["yes", "no"]:
    decision = input("Please enter yes or no: ").lower()

# If the decision is "no", exit the program
if decision == "no":
    print("Okay, see you later!")
    exit()

# Define the drink menu items with their descriptions and prices
Drink_Menu = [
    "Espresso: $3, A concentrated shot of pure coffee \n",
    "Cappuccino: $4, Espresso with steamed milk and foam \n",
    "Latte: $5, Espresso with steamed milk and a light layer of foam \n",
    "Americano: $3, Espresso diluted with hot water \n",
    "Hot Chocolate: $2, A rich, creamy chocolate beverage \n",
    "Tea: $2, A variety of hot tea options \n",
    "Milk Shake: $3, A thick, cold beverage made with milk and ice cream \n",
    "Mocha: $4, Espresso with steamed milk and chocolate \n",
    "Coffee: $3, A classic brewed coffee \n",
]

# Define the food menu items with their descriptions and prices
Food_Menu = [
    "French Fries: $5, Crispy, golden-brown fried potato strips \n",
    "Burger: $10, A sandwich with a patty, bun, and various toppings \n",
    "Pizza: $15, A flatbread topped with tomato sauce, cheese, and various toppings \n",
    "Chicken Wings: $5, Crispy, saucy chicken wings \n",
    "Sandwich: $7, A variety of fillings between two slices of bread \n",
    "Pasta: $15, Various types of pasta dishes \n",
    "Risotto: $15, A creamy, rice-based dish with vegetables or meat \n",
    "Ramen: $20, A Japanese noodle soup with broth, noodles, and toppings \n",
    "Sushi: $25, Vinegared rice rolls with various fillings \n",
]
# Define the complete menu list
menu = [
    "Espresso", "Cappuccino", "Latte", "Americano", "Hot Chocolate",
    "Tea", "Milk Shake", "Mocha", "Coffee", "French Fries",
    "Burger", "Pizza", "Chicken Wings", "Sandwich", "Pasta",
    "Risotto", "Ramen", "Sushi"
]

# Convert menu items to lowercase for case-insensitive matching
menu = [menu_item.lower() for menu_item in menu]

# Define a class for the menu item object
class Menu_Object:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
        self.orders = []  # Initialize an empty list to store orders

    # Creating a function under the Menu_Object class to get the name of the menu item
    def get_name(self, decision):
        if decision == "yes":
            # Display the food and drinks menu
            print(Fore.YELLOW + "Food Menu:")
            print(Fore.YELLOW + "\n".join(Food_Menu))
            print(Fore.YELLOW + "Drinks Menu:")
            print(Fore.YELLOW + "\n".join(Drink_Menu))
            
            self.orders = []  # Reset the orders list
            order = input("What would you like to order? ").lower()
            
            # Prompt for orders until the user types "done"
            while order != "done":
                if order in menu:
                    self.orders.append(order)  # Add the valid order to the orders list
                else:
                    print("Please choose from the menu provided.")
                    print()
                    time.sleep(1)
                order = input("What would you like to order? (Type done to stop): ").lower()
            
            self.name = order  # Set the name of the menu item to the last order
            
            # Set the price of the menu item based on the index in the menu list
            if order in menu:
                index = menu.index(order)
                self.price = Drink_Menu[index] if index < len(Drink_Menu) else Food_Menu[index - len(Drink_Menu)]
    
    # Creates a function to calculate the total cost of the menu item
    def calculate_total(self, orders):
        total = 0
        for order in orders:
            index = menu.index(order)
            price = Drink_Menu[index] if index < len(Drink_Menu) else Food_Menu[index - len(Drink_Menu)]
            
            # Extract the price from the menu item and accumulate the total
            total += float(price.split(": $")[1].split(",")[0])
        
        return total
    
    def get_price(self, decision):
        if decision == "yes":
            total_cost = self.calculate_total(self.orders)
            
            # Display the total cost and prompt for payment
            print("You have to pay $:", total_cost)
            self.price = input("Press any key and ENTER to pay! ")
            print("Thank you for your order! Come back soon!")


# Create an instance of the Menu_Object class
Menu_Item = Menu_Object("", "", "")

# Call the methods based on the user's decision
Menu_Item.get_name(decision)
Menu_Item.get_price(decision)