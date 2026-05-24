import time
import random
from tkinter import *
from settings import SettingsWindow, themes

def get_text():
    # Open file and read lines, stripping whitespace and ignoring empty lines
    try:
        with open("text.txt", "r") as file:
            paragraph_pool = [line.strip() for line in file if line.strip()]
        return random.choice(paragraph_pool)  
    except FileNotFoundError:
        # If the file is not found, return a default paragraph to ensure the application still works
        return "The quick brown fox jumps over the lazy dog. Text file was not found."  

def check_text(original_paragraph, user_input, time_taken):
    split_paragraph = original_paragraph.split() # Split the original paragraph into words for checking one by one
    split_user_input = user_input.split() # Split the user's input into words for checking one by one

    # Count the number of correct words by comparing the original and user input word by word
    correct_words = sum(1 for o, u in zip(split_paragraph, split_user_input) if o == u) 
    total_words = len(split_paragraph)
    score = (correct_words / total_words) * 100 # Calculate the score as a percentage of correct words
    
    # Safe guard against zero time or empty input to prevent crashes
    if time_taken > 0 and len(split_user_input) > 0:
        wpm = (correct_words / time_taken) * 60 # Calculate words per minute based on the user's input and time taken
    else:
        wpm = 0.00

    result_label.config(text=f"Your score: {score:.2f}% | WPM: {wpm:.2f} | Time taken: {time_taken:.2f} seconds") # Update the label with the score, WPM, and time taken
    start_button.config(state=NORMAL) # Re-enable the start button for the next test

def start_test():
    start_button.config(state=DISABLED) # Disable the start button to prevent multiple tests at once
    
    # Get a random paragraph and display it in the label
    paragraph = get_text() 
    paragraph_label.config(text=paragraph)

    input_entry.delete(0, END) # Clear the input entry for new input
    input_entry.focus() # Set cursor focus to the entry box automatically
    start_time = time.time() # Record the start time of the test

    def on_enter(event):
        end_time = time.time() # Record the end time when the user presses Enter
        time_taken = end_time - start_time # Calculate the time taken for the test
        user_input = input_entry.get().strip() # Get the user's input from the entry widget and strip any leading/trailing whitespace

        # Check the user's input against the original paragraph and update the result label
        check_text(paragraph, user_input, time_taken) 

    input_entry.bind("<Return>", on_enter) # Bind the Enter key to trigger the on_enter function when pressed

def apply_settings(config):
    # Retrieve colors dynamically from the processed config payload
    bg_color = config["bg"]
    text_color = config["text"]
    
    # Apply to Main Window
    root.config(bg=bg_color) 
    
    # Apply to App Widgets dynamically to maintain contrast visibility
    welcome_label.config(bg=bg_color, fg=text_color)
    paragraph_label.config(bg=bg_color, fg=text_color)
    result_label.config(bg=bg_color, fg=text_color)
    start_button.config(
        bg=themes[config["theme"]].get("button_bg", "#FF7D40"), 
        fg=text_color, 
        activebackground=themes[config["theme"]].get("button_bg", "#FF7D40"),
        bd=1, relief=SOLID # <-- Gives it a crisp, themed border
    )
    settings_button.config(
        bg=themes[config["theme"]].get("button_bg", "#FF7D40"), 
        fg=text_color, 
        activebackground=themes[config["theme"]].get("button_bg", "#FF7D40"),
        bd=1, relief=SOLID # <-- Consistent styling with the start button for a cohesive look
    )
    
    # Input field handling: Base white bg with matching text, 
    # except when using Dark or Sci-Fi modes where an entry box looks cleaner muted.
    if config["theme"] in ["Dark", "Sci-Fi"]:
        input_entry.config(bg="#1E1E1E", fg=text_color, insertbackground=text_color) # insertbackground fixes the flashing cursor color
    else:
        input_entry.config(bg="white", fg="black", insertbackground="black")

# -- GUI Setup --
root = Tk()
root.title("Typing Test")
root.geometry("600x500")
root.config(padx=20, pady=20,bg="#FF7D40") # Set the background color of the window to a bright orange for a more vibrant look

settings_window = SettingsWindow(root, apply_settings) # Create an instance of the settings window, passing the apply_settings function as a callback

# Settings button to open the settings window, styled with a background color that matches the default theme for consistency
settings_button = Button(root, text="⚙ Settings", command=lambda: settings_window.create_window())
settings_button.pack(padx=10,side='top',anchor='nw')

welcome_label = Label(root, text="Welcome to the Typing Test!", font=("Arial", 16), bg="#FF7D40")
welcome_label.pack(pady=10)

# Label to display the paragraph for the typing test, with a wrap length of 500 pixels for better readability
paragraph_label = Label(root, text="", wraplength=500, font=("Arial", 14), bg="#FF7D40")
paragraph_label.pack(pady=20)

input_entry = Entry(root, width=60, font=("Arial", 12), bg="white", relief=FLAT) 
input_entry.pack(pady=10, ipady=5) # Increase the internal padding of the entry widget for a more comfortable typing experience

result_label = Label(root, text="", font=("Arial", 12), bg="#FF7D40")
result_label.pack(pady=10)

start_button = Button(root, text="Start Test", command=lambda: start_test())
start_button.pack(pady=10)

if __name__ == "__main__":
    root.mainloop()