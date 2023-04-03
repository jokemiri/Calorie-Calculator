import tkinter as tk

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

# define a function to add a food item and its quantity to the total calories
def add_food_item():
    global total_calories
    food_item = food_item_var.get().lower()
    quantity = int(quantity_var.get())
    total_calories += calories[food_item] * quantity
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
quantity_var.set("1")
quantity_entry = tk.Entry(root, textvariable=quantity_var)
quantity_entry.pack()

add_button = tk.Button(root, text="Add Item", command=add_food_item)
add_button.pack()

total_calories_label = tk.Label(root, text="Total Calories: {}".format(total_calories))
total_calories_label.pack()

# start the GUI event loop
root.mainloop()
