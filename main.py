"""
Created on Jan. 22, 2024

A python that will do something cool.

@author jackholy
"""

# Flow layout for a dynamic window sizes.
# Create a front-end and a back-end and connect them.
# Set up your GUI (front-end) as an object.
# Extend the tkinter class.
# They're looking for overall functionality. Widgets that respond to one another and react together.
# When in doubt look at the tkinter docs.


import tkinter as tk


def main():
    # Create the primary window
    mainWindow = tk.Tk()
    # Set the window size
    mainWindow.geometry("400x300")

    label = tk.Label(mainWindow, text="Hello World!", font=("Times New Roman", 16))
    label.pack(pady=20)
    mainWindow.mainloop()


if __name__ == "__main__":
    main()
