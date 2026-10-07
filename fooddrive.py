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

        file.write("\nPANTRY ITEMS\n")
for item in pantry_only:
            file.write(f"{item},0\n")

print("Inventory file is ready.")


#Class Product

class Product:
    def __init__(self, name, points, qty):
        self.name
        self.points