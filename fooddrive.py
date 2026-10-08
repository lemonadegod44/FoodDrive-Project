import os.path

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
    with open("inventory.txt", "w") as file:

        for item in basket_items:
            file.write(f"{item},0\n")

        for item in pantry_only:
            file.write("\nPANTRY ITEMS\n")
            file.write(f"{item},0\n")


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

    #Add Product
    def add_product(self,product):
        #checks to see if an item already exists
            for p in self.products:                
                if p.name.lower() == product.name.lower():
                    print (f"Product {product.name} already exists.")
                    return


            self.products.append(product)
            print(f"Product {product.name} has been successfully added.")
    
    #View Products
    def view_products(self):
        if not self.products:
            print("The inventory is empty.")
        
        else:
            print("-----INVENTORY LIST-----")
            for product in self.products:
                product.display_info()




    #Update Stock Check
    def update_stock(self, name, change):
        for product in self.products:
            if product.name.lower() == name.lower():
                product.update_stock(change)
                return
        print(f"Product {name} stock is not available in inventory.")




#Test

p1 = Product("Frozen Ham", 50, 1)
p2 = Product("Canned Meats", 10, 1)


store = Inventory()
store.add_product(p1)
store.add_product(p2)

store.update_stock("Frozen Ham", 14)
store.update_stock("Ball", 14)

#store.view_products()

"""
p1.display_info()
p2.display_info()
p1.update_stock(12)
p1.display_info()
"""