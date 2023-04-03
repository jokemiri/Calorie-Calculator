import tkinter as tk
from tkinter import ttk

# define a dictionary to store the calorie information for different foods
calories = {
    "apple": 52,
    "banana": 89,
    "orange": 47,
    "grapefruit": 52,
    "carrot": 41,
    "celery": 6,
    "cucumber": 16,
    "tomato": 22
}

# initialize the total calories to zero
total_calories = 0

# define a function to convert grams to calories
def grams_to_calories(grams, calorie_per_100g):
    return (grams / 100) * calorie_per_100g

# define a function to add a food item and its quantity to the total calories
def add_food_item():
    global total_calories
    food_item = food_item_var.get().lower()
    quantity = quantity_var.get()
    quantity_grams = int(quantity.split(" ")[0])
    calorie_per_100g = calories[food_item]
    calories_for_quantity = grams_to_calories(quantity_grams, calorie_per_100g)
    total_calories += calories_for_quantity
    total_calories_label.config(text="Total Calories: {}".format(total_calories))

# create the main window and set its properties
root = tk.Tk()
root.title("Calorie Counter")
root.geometry("300x200")

# create the GUI elements
food_item_label = tk.Label(root, text="Food Item:")
food_item_label.pack()
food_item_var = tk.StringVar(root)
food_item_var.set("Apple")
food_item_dropdown = tk.OptionMenu(root, food_item_var, *calories.keys())
food_item_dropdown.pack()

quantity_label = tk.Label(root, text="Quantity:")
quantity_label.pack()
quantity_var = tk.StringVar(root)
quantity_var.set("100 g")
quantity_options = ["100 g", "200 g", "300 g", "400 g", "500 g"]
quantity_combobox = tk.ttk.Combobox(root, values=quantity_options, textvariable=quantity_var, state="readonly")
quantity_combobox.pack()

add_button = tk.Button(root, text="Add Item", command=add_food_item)
add_button.pack()

total_calories_label = tk.Label(root, text="Total Calories: {}".format(total_calories))
total_calories_label.pack()

# start the GUI event loop
root.mainloop()
