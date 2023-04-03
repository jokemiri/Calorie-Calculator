import tkinter as tk

food_calories = {
    'Apple': 0.52,
    'Banana': 0.89,
    'Orange': 0.47,
    'Grapes': 0.69,
    'Chicken Breast': 1.49,
    'Salmon Fillet': 2.08,
    'Beef Steak': 2.21,
    'Pasta': 1.27,
    'Rice': 1.06,
    'Bread': 2.54,
}
   
# Define the calorie calculator function
def calculate_calories():
    # Get the selected food item and quantity from the GUI
    food_item = food_items.get()
    quantity = quantity_input.get()

    # Calculate the total calories
    calories = food_calories[food_item] * float(quantity)

    # Update the calories label in the GUI
    calories_label.config(text=f"{calories:.2f} calories")

# Create the main window
root = tk.Tk()
root.title("Calorie Calculator")
root.geometry("300x200")

# Create the food item selection dropdown menu
food_items = tk.StringVar()
food_items.set('Apple')
food_dropdown = tk.OptionMenu(root, food_items, *food_calories.keys())
food_dropdown.pack(pady=10)

# Create the quantity input field
quantity_label = tk.Label(root, text="Quantity (grams):")
quantity_label.pack()
quantity_input = tk.Entry(root)
quantity_input.pack()

# Create the calculate button
calculate_button = tk.Button(root, text="Calculate Calories", command=calculate_calories)
calculate_button.pack(pady=10)

# Create the calories label
calories_label = tk.Label(root, text="0 calories")
calories_label.pack()

def total_dict():
    total = {(food_items.get)}
    sum_total = sum(total.values())
    return sum_total

# Start the main event loop
root.mainloop()
