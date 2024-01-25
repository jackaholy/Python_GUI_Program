"""
Created on Jan. 24, 2024

@author jackholy
"""

import random
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Had help from https://chat.openai.com/
def load_names_from_file(file):
    try:
        with open(file, "r") as file:
            names = [line.strip() for line in file]  # Remove any trailing whitespace
        return names
    # Make sure the file exists
    except FileNotFoundError:
        messagebox.showerror("File Not Found", f"The file '{file}' was not found.")
        return []

# Generate numbers 1 through 1000 and shuffle them
def generate_random_numbers():
    numbers = list(range(1, 1001))
    random.shuffle(numbers)
    return numbers


class TerribleUI:
    def __init__(self, main_window):
        # Create window
        self.warning_label = None
        self.main = main_window
        self.main.title("Worst UI Ever")

        # Create a StringVar to hold the selected "age" value
        self.dropdown_var = tk.StringVar(self.main)

        # Headers above widget for names
        self.name_title_label = tk.Label(self.main, text="Please Enter Your Name: ", font=('Times New Roman', 16))
        self.name_title_label.place(x=10, y=5)

        # Load first_names.txt from the file
        self.first_names = load_names_from_file("first_names.txt")

        # First name label
        self.first_name = tk.Label(self.main, text="First Name: ", font=('Times New Roman', 14))
        self.first_name.place(x=14, y=40)
        # Selected first name
        self.selected_first_name_label = tk.Label(self.main, text="", font=('Times New Roman', 14))
        self.selected_first_name_label.place(x=90, y=40)
        # First name button
        self.select_button = tk.Button(self.main, text="Pick First Name", command=self.select_first_name)
        self.select_button.place(x=20, y=70)

        # Load last_names.txt.txt from the file
        self.last_names = load_names_from_file("last_names.txt")

        # Last name label
        self.last_name = tk.Label(self.main, text="Last Name: ", font=('Times New Roman', 14))
        self.last_name.place(x=14, y=100)
        # Selected last name
        self.selected_last_name_label = tk.Label(self.main, text="", font=('Times New Roman', 14))
        self.selected_last_name_label.place(x=90, y=100)
        # Last name button
        self.select_button = tk.Button(self.main, text="Pick Last Name", command=self.select_last_name)
        self.select_button.place(x=20, y=130)

        # Headers above widget for age
        self.age_title_label = tk.Label(self.main, text="Please Select Your Age: ", font=('Times New Roman', 16))
        self.age_title_label.place(x=300, y=5)
        # Generate random numbers
        self.random_numbers = generate_random_numbers()
        self.dropdown_var = tk.StringVar(self.main)
        # Don't allow the user to enter their own age. Force them to find it
        self.dropdown = ttk.Combobox(self.main, values=self.random_numbers, state="readonly")
        self.dropdown.set("Select An Age...")
        # Age drop down menu
        self.dropdown.bind("<<ComboboxSelected>>", self.on_dropdown_change)
        self.dropdown.place(x=280, y=50)

        # Button to submit selected name and age
        self.submit_button = tk.Button(self.main, text="Submit", command=self.submit_info)
        self.submit_button.place(x=20, y=200)

        # Display chosen credentials
        self.display_label = tk.Label(self.main, text="", font=('Times New Roman', 14))
        self.display_label.place(x=300, y=200)

    # Allow the user to save the selected age
    def on_dropdown_change(self, event):
        selected_value = self.dropdown_var.get()
        self.dropdown_var.set(selected_value)

    def submit_info(self):
        # Get the selected first name, last name, and age
        selected_first_name = self.selected_first_name_label.cget("text")
        selected_last_name = self.selected_last_name_label.cget("text")
        selected_age = self.dropdown_var.get()

        # Display the chosen information
        info_text = f"Submitted Information:\nFirst Name: {selected_first_name}\nLast Name: {selected_last_name}\nAge: {selected_age}"
        self.display_label.config(text=info_text)

        # Display Identity theft disclaimer
        self.warning_label = tk.Label(self.main,
                                      text="(Identity theft carries a maximum term of 15 years' imprisonment, a fine, and cri"
                                           "minal forfeiture of any personal property used or intended to be "
                                           "used to commit the offense)", font=('Times New Roman', 7))
        self.warning_label.place(x=5, y=270)

    # Select and display a random first name from the list
    def select_first_name(self):
        if self.first_names:
            selected_name = random.choice(self.first_names)
            self.selected_first_name_label.config(text=f"{selected_name}")
        else:
            messagebox.showinfo("Empty List", "The list of first_names.txt is empty.")

    # Select and display a random last name from the list
    def select_last_name(self):
        if self.last_names:
            selected_name = random.choice(self.last_names)
            self.selected_last_name_label.config(text=f"{selected_name}")
        else:
            messagebox.showinfo("Empty List", "The list of last_names.txt is empty.")


if __name__ == "__main__":
    # Create window
    wn = tk.Tk()
    window_width = 500
    window_height = 300

    # Get screen width and height
    screen_width = wn.winfo_screenwidth()
    screen_height = wn.winfo_screenheight()

    # Calculate x and y coordinates for the window to be centered
    x_coordinate = (screen_width - window_width) // 2
    y_coordinate = (screen_height - window_height) // 4

    # Set window geometry
    wn.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
    # Create an instance of the TerribleUI
    TerribleUI(wn)
    wn.mainloop()
