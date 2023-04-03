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
    food_item_entry = "{}: {}".format(food_item.capitalize(), quantity)
    food_items_listbox.insert(tk.END, food_item_entry)

# create the main window and set its properties
root = tk.Tk()
root.title("Calorie Counter")
root.geometry("400x250")
root.config(bg='#087b7b')
root.resizable(False, False)

# set an icon for the window
# set the window icon
root.iconbitmap("icon.ico")

# create the GUI elements
food_item_label = tk.Label(root, text="Food Item:", font='Raleway', bg='#087b7b', fg='white')
food_item_label.place(x=10, y=10)
food_item_var = tk.StringVar(root)
food_item_var.set("Apple")
food_item_dropdown = tk.OptionMenu(root, food_item_var, *calories.keys())
food_item_dropdown.place(x=10, y=30)

quantity_label = tk.Label(root, text="Quantity:", font='Raleway', bg='#087b7b', fg='white')
quantity_label.place(x=10, y=80)

def increment_quantity():
    quantity = quantity_var.get()
    quantity_grams = int(quantity.split(" ")[0])
    new_quantity_grams = quantity_grams + 1
    new_quantity = "{} g".format(new_quantity_grams)
    quantity_var.set(new_quantity)

increment_button = tk.Button(root, text="Increase", font='Raleway', command=increment_quantity)
increment_button.place(x=10, y=100)

#Login frame
frame=tk.Frame(root, width=200, height=350, bg="white")
frame.place(x=200, y=0)

quantity_var = tk.StringVar(root)
quantity_var.set("5 g")
quantity_combobox = tk.ttk.Combobox(root, textvariable=quantity_var, values=[f"{i} g" for i in range(5, 101)])
quantity_combobox.place(x=10, y=140)

add_button = tk.Button(root, text="Add Item", font='Raleway', command=add_food_item, bg='#3D7C3C', fg='white')
add_button.place(x=2, y=200)

total_calories_label = tk.Label(frame, text="Total Calories: {}".format(total_calories), font='Raleway', bg='white', fg='#087b7b')
total_calories_label.place(x=0, y=0)

# add a listbox widget to display the added food items
food_items_listbox = tk.Listbox(root, width=30, height=13)
food_items_listbox.place(x=210, y=20)

# add a function to remove the selected item from the listbox
def remove_food_item():
    global total_calories
    selected_index = food_items_listbox.curselection()
    if selected_index:
        selected_item = food_items_listbox.get(selected_index)
        selected_quantity_grams = int(selected_item.split(":")[1].strip().split(" ")[0])
        selected_food_item = selected_item.split(":")[0]
        selected_calorie_per_100g = calories[selected_food_item.lower()]
        selected_calories_for_quantity = grams_to_calories(selected_quantity_grams, selected_calorie_per_100g)
        total_calories -= selected_calories_for_quantity
        total_calories_label.config(text="Total Calories: {}".format(total_calories), font='Raleway')
        food_items_listbox.delete(selected_index)

remove_button = tk.Button(root, text="Remove Item", font='Raleway', width=10, command=remove_food_item, bg='#7B0808', fg='white')
remove_button.place(x=88, y=200)

# run the main loop
root.mainloop()
