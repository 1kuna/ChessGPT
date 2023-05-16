import tkinter as tk
import pgn_parse

# Create a new window
window = tk.Tk()

# Set the window title
window.title("My Extension")

# Add a label to the window
label = tk.Label(window, text="Best move: " + str(pgn_parse.get_best_move()))
label.pack()

# Start the main event loop
window.mainloop()