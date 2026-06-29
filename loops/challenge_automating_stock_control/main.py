# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100
print("Processing started")
for item in inventory:
    values = inventory[item]
    print(f"Processing {item}")
    current_stock = values[0]
    minimum_stock = values[1]
    restock_quantity = values[2]
    sale_status = values[3]
    while current_stock < minimum_stock:
        current_stock = current_stock + restock_quantity
        inventory[item][0] = current_stock
#        print(current_stock)
    if sale_status == False:
        if current_stock > discount_threshold:
            sale_status = True
            inventory[item][3] = True
print("Processing completed")



