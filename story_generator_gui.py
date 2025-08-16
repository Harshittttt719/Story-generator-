import tkinter as tk
from tkinter import ttk, messagebox
import random

# Sample Data
genres = ["Romance", "Sci-Fi", "Fantasy", "Horror", "Comedy", "Thriller"]
themes = ["Betrayal", "Survival", "Redemption", "Love", "Revenge", "Coming of Age"]
characters = ["Time-traveling scientist", "Talking dog", "Witch in training", "AI gone rogue", "Lost child", "Retired soldier"]

# Prompt Generator Function
def generate_prompt():
    genre = genre_var.get()
    theme = theme_var.get()
    character = character_var.get()

    if not genre or not theme or not character:
        messagebox.showwarning("Input Missing", "Please select all fields!")
        return

    prompt = f"In a {genre.lower()} world, a {character.lower()} faces the challenge of {theme.lower()}, uncovering secrets that could change everything."
    result_text.config(state='normal')
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, prompt)
    result_text.config(state='disabled')

def clear_all():
    genre_var.set("")
    theme_var.set("")
    character_var.set("")
    result_text.config(state='normal')
    result_text.delete(1.0, tk.END)
    result_text.config(state='disabled')

def surprise_me():
    genre_var.set(random.choice(genres))
    theme_var.set(random.choice(themes))
    character_var.set(random.choice(characters))

# GUI Setup
root = tk.Tk()
root.title("Story Idea Generator")
root.geometry("600x400")
root.configure(bg="#1e1e1e")  # Dark background
root.resizable(False, False)

# Title
tk.Label(root, text="🎬 Story Idea Generator", font=("Helvetica", 18, "bold"), bg="#1e1e1e", fg="white").pack(pady=10)

# Form Frame
form_frame = tk.Frame(root, bg="#1e1e1e")
form_frame.pack(pady=10)

# Genre
genre_var = tk.StringVar()
tk.Label(form_frame, text="Select Genre:", font=("Helvetica", 12), bg="#1e1e1e", fg="white").grid(row=0, column=0, padx=10, pady=5, sticky='w')
genre_menu = ttk.Combobox(form_frame, textvariable=genre_var, values=genres, state='readonly')
genre_menu.grid(row=0, column=1)

# Theme
theme_var = tk.StringVar()
tk.Label(form_frame, text="Select Theme:", font=("Helvetica", 12), bg="#1e1e1e", fg="white").grid(row=1, column=0, padx=10, pady=5, sticky='w')
theme_menu = ttk.Combobox(form_frame, textvariable=theme_var, values=themes, state='readonly')
theme_menu.grid(row=1, column=1)

# Character
character_var = tk.StringVar()
tk.Label(form_frame, text="Select Character Type:", font=("Helvetica", 12), bg="#1e1e1e", fg="white").grid(row=2, column=0, padx=10, pady=5, sticky='w')
character_menu = ttk.Combobox(form_frame, textvariable=character_var, values=characters, state='readonly')
character_menu.grid(row=2, column=1)

# Buttons
button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=10)

button_style = {"bg": "#000000", "fg": "white", "activebackground": "#333333", "activeforeground": "white", "padx": 10}

tk.Button(button_frame, text="Generate", command=generate_prompt, **button_style).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Clear", command=clear_all, **button_style).grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="Surprise Me", command=surprise_me, **button_style).grid(row=0, column=2, padx=10)

# Result Box
result_text = tk.Text(root, height=5, width=65, wrap="word", font=("Helvetica", 11), bg="black", fg="white", insertbackground="white")
result_text.pack(pady=10)
result_text.config(state='disabled')

# Mainloop
root.mainloop()
