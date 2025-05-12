import tkinter as tk
from tkinter import messagebox
import numpy as np
import joblib

# Load model and column names
model = joblib.load('real_estate_price_model.pkl')
columns = joblib.load('columns.pkl')

# Extract location names (one-hot encoded cols start from index 3)
locations = columns[3:]

# Define prediction function (copied from your notebook)
def predict_price(location, sqft, bath, bhk):
    try:
        loc_index = np.where(np.array(columns) == location)[0][0]
        x = np.zeros(len(columns))
        x[0] = sqft
        x[1] = bath
        x[2] = bhk
        if loc_index >= 0:
            x[loc_index] = 1
        return model.predict([x])[0]
    except Exception as e:
        return f"Error: {e}"

# Create main GUI window
root = tk.Tk()
root.title("Real Estate Price Predictor")
root.geometry("400x400")

# User input fields
inputs = {}

tk.Label(root, text="Total Sqft:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky='w')
sqft_entry = tk.Entry(root, width=20, font=("Arial", 12))
sqft_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Bath:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10, sticky='w')
bath_entry = tk.Entry(root, width=20, font=("Arial", 12))
bath_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="BHK:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10, sticky='w')
bhk_entry = tk.Entry(root, width=20, font=("Arial", 12))
bhk_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Location:", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=10, sticky='w')
location_var = tk.StringVar(root)
location_var.set(locations[0])  # Default location
location_dropdown = tk.OptionMenu(root, location_var, *locations)
location_dropdown.config(font=("Arial", 12))
location_dropdown.grid(row=3, column=1, padx=10, pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14), fg="green")
result_label.grid(row=5, column=0, columnspan=2, pady=20)

# Predict button function
def on_predict():
    try:
        sqft = float(sqft_entry.get())
        bath = int(bath_entry.get())
        bhk = int(bhk_entry.get())
        location = location_var.get()
        price = predict_price(location, sqft, bath, bhk)
        result_label.config(text=f"Predicted Price: ₹{price:,.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Predict button
tk.Button(root, text="Predict", command=on_predict, font=("Arial", 12), bg="blue", fg="white").grid(
    row=4, column=0, columnspan=2, pady=10
)

root.mainloop()
