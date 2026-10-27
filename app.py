import os.path
from datetime import datetime

#Inventory Items

basket_items = {"Frozen Ham": 50,
                "Frozen Turket": 50,
                "Canned Yams": 5,
                "Canned Corn": 5,
                "Canned Green Beans": 5,
                "Canned Carrots": 5,
                "Canned Peas": 5,
                "Canned Fruit": 5,
                "Canned Pumpkin": 5,
                "Canned Milk": 5,
                "Instant Mashed Potatoes": 8,
                "Potatoes": 5,
                "Sugar": 15,
                "Flour": 10,
                "Cranberry Sauce": 5,
                "Pie Crust": 8,
                "Pie Filling": 5,
                "Stuffing Mix": 10,
                "Gravy Mix": 1,
                "Bread Mix": 5,
                "Cookie Mix": 5,
                "Cake Mix and Icing": 5,
                "Cooking Oil": 8,
                "Mac N Cheese": 2
                }

pantry_only = {"Canned Meats": 10,
                "Peant Butter": 8,
                "Boxed Meal Kits": 5,
                "Canned Soup": 5,
                "Quick Meals": 1 
                }

#File update
if not os.path.exists("inventory.txt"):
    with open("inventory.txt","w") as file:

        file.write("BASKET ITEMS\n")

        for item, points in basket_items.items():
            file.write(f"{item},{points},0\n")

        file.write("\nPANTRY ITEMS\n")

        for item, points in pantry_only.items():
            file.write(f"{item},{points},0\n")
    
    print("File has been created.")

#Class Product

class Product:

    def __init__(self, name, points, qty):
        self.name = name
        self.points = points
        self.qty = qty
    #Display Info
    def display_info(self):
        print(f"{self.name:<15} Points: {self.points:<10} Stock: {self.qty}")

    #Update Stock
    def update_stock(self, update):
        self.qty += update
        print(f"Stock updated for {self.name}, the updated stock is {self.qty}.")

#Class Inventory
class Inventory:
    #Save Products
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    #Add Product
    def add_product(self,product):
        #checks to see if an item already exists
        for p in self.products:                
            if p.name.lower() == product.name.lower():
                print (f"Product {product.name} already exists.")
                return

        #Adds product if doesn't exist
        self.products.append(product)
    
    #View Products
    def view_products(self):
        if not self.products:
            print("The inventory is empty.")
            return
        
        print("-----INVENTORY LIST-----")
        for product in self.products:
            product.display_info()




    #Update Stock Check
    def update_stock(self, name, change):
        for product in self.products:
            if product.name.lower() == name.lower():
                product.update_stock(change)

        #Automatically Save
        self.save_inventory()
        return

        print(f"Product {name} stock is not available in inventory.")

    #Total Inventory Value
    def total_inventory_value(self):
        total = 0
        for product in self.products:
            total += product.points * product.qty
        print(f"Total inventory value is {total}")


    #Save Inventory
    def save_inventory(self):
        save_time = datetime.now().astimezone().strftime(
            "%m/%d/%Y %I:%M:%S %p"
        )

        with open("inventory.txt", "w") as file:

            #Save basket items
            file.write("BASKET ITEMS\n")

            for product in self.products:
                if product.name in basket_items:
                    file.write(
                        f"{product.name},{product.points},{product.qty}\n"
                    )
            #Save pantry items
            file.write("\nPANTRY ITEMS\n")

            for product in self.products:
                if product.name in pantry_only:
                    file.write(
                        f"{product.name},{product.points},{product.qty}\n"
                    )
        
        print(f"Inventory successfully saved at {save_time}")



store = Inventory()


#Add basket items to inventory
for items, points in basket_items.items():
    product = Product(items, points, 0)
    store.add_product(product)

#Add pantry items to inventory
for items, points in pantry_only.items():
    product = Product(items, points, 0)
    store.add_product(product)


#Food Inventory
while True:
    print("-----------FOOD DRIVE-----------")
    print("1.Add Item")
    print("2.Update Stock")
    print("3.View Items")
    print("4.Total Inventory Value")
    print("5.Exit")


    #User Input
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Food Name: ")
        points = float(input("Points: "))
        qty = int(input("Quantity: "))
        product = Product(name, points, qty)
        store.add_product(product)

    elif choice == "2":
        name = input("Product Name: ")
        change = int(input("Quantity to add/remove: "))
        store.update_stock(name,change)

    elif choice == "3":
        store.view_products()

    elif choice == "4":
        store.total_inventory_value()
    
    elif choice == "5":
        print("Exiting Inventory.")
        break

    else:
        print("Invalid choice.")