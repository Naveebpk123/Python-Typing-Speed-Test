from tkinter import *
from tkinter import ttk

# Precise theme palette definitions
themes = {
    "Default": {"bg": "#FF7D40", "text": "#000000", "button_bg": "#FF7D40"}, 
    "Dark": {"bg": "#2B2B2B", "text": "#FFFFFF", "button_bg": "#333333"}, 
    "Light": {"bg": "#FAFAFA", "text": "#1A1A1A", "button_bg": "#E0E0E0"}, 
    "Sci-Fi": {"bg": "#0D1B2A", "text": "#00E5FF", "button_bg": "#1A1A1A"} 
}

# Mapping user-friendly names to Hex codes for individual color choices
COLOR_MAP = {
    "Orange": "#FF7D40",
    "Blue": "#4A90E2",
    "Green": "#2ECC71",
    "Purple": "#9B5DE5",
    "Light": "#FAFAFA",
    "Dark Charcoal": "#2B2B2B",
    "Black": "#000000",
    "White": "#FFFFFF",
    "Red": "#E74C3C",
    "Neon Cyan": "#00E5FF",
    "Deep Navy": "#0D1B2A"
}

# Reverse map to find name from Hex code
REV_COLOR_MAP = {v: k for k, v in COLOR_MAP.items()}

class SettingsWindow:
    # This class manages the settings window where users can customize themes and colors
    def __init__(self, main_root, apply_callback):
        self.main_root = main_root
        self.apply_callback = apply_callback
        self.window = None

    def create_window(self):
        # Prevent opening duplicate settings windows
        if self.window is not None and self.window.winfo_exists():
            self.window.lift() # Bring the existing window to the front if it's already open
            return

        self.window = Toplevel(self.main_root)
        self.window.title("⚙ Settings")
        self.window.geometry("350x450")
        self.window.config(pady=10, padx=10)
        
        # Initialize StringVars to hold the current selections for background, text, and theme
        self.bg_var = StringVar(value="Orange")
        self.text_var = StringVar(value="Black")
        self.theme_var = StringVar(value="Default")
        
        # --- THEME SELECTION ---
        Label(self.window, text="Overall Theme:", font=("Arial", 10, "bold")).pack(pady=5)
        self.theme_dropdown = ttk.Combobox(self.window, textvariable=self.theme_var, state="readonly")
        self.theme_dropdown['values'] = list(themes.keys())
        self.theme_dropdown.pack(pady=5)
        
        # When user clicks a theme, update the individual Bg and Text dropdowns automatically
        self.theme_dropdown.bind("<<ComboboxSelected>>", self.handle_theme_change)

        # --- INDIVIDUAL SELECTIONS ---
        Label(self.window, text="Custom Background Color:").pack(pady=5)
        self.bg_dropdown = ttk.Combobox(self.window, textvariable=self.bg_var, state="readonly")
        self.bg_dropdown['values'] = ('Orange', 'Blue', 'Green', 'Purple', 'Light', 'Dark Charcoal', 'Deep Navy')
        self.bg_dropdown.pack(pady=5)

        Label(self.window, text="Custom Text Color:").pack(pady=5)
        self.text_dropdown = ttk.Combobox(self.window, textvariable=self.text_var, state="readonly")
        self.text_dropdown['values'] = ('Black', 'White', 'Red', 'Blue', 'Neon Cyan')
        self.text_dropdown.pack(pady=5)

        # --- QUICK ACTION BUTTONS ---
        # Styling buttons with specific background highlights
        self.dark_mode_btn = Button(self.window, text="🌙 Dark Mode", bg="#2B2B2B", fg="white", 
                                    activebackground="#333333", command=self.enable_dark_mode)
        self.dark_mode_btn.pack(pady=8, fill=X, padx=40)
        
        self.reset_btn = Button(self.window, text="🔄 Reset to Default", bg="#FF7D40", fg="black", 
                                activebackground="#FF945B", command=self.reset_defaults)
        self.reset_btn.pack(pady=8, fill=X, padx=40)
        
        # --- SAVE ---
        self.save_btn = Button(self.window, text="Apply Changes", font=("Arial", 11, "bold"), 
                               bg="#2ECC71", fg="white", command=self.save_settings)
        self.save_btn.pack(pady=20)

    def handle_theme_change(self, event=None):
        """Forces the background and text dropdowns to match the selected theme preset."""
        selected_theme = self.theme_var.get()
        theme_data = themes[selected_theme]
        
        # Translate theme hex codes back into readable dropdown names
        bg_name = REV_COLOR_MAP.get(theme_data["bg"], "Orange")
        text_name = REV_COLOR_MAP.get(theme_data["text"], "Black")
        
        self.bg_var.set(bg_name)
        self.text_var.set(text_name)

    def enable_dark_mode(self):
        self.theme_var.set("Dark")
        self.handle_theme_change()
        
    def reset_defaults(self):
        self.theme_var.set("Default")
        self.handle_theme_change()

    def save_settings(self):
        # Convert chosen names to functional Hex values
        bg_hex = COLOR_MAP.get(self.bg_var.get(), "#FF7D40")
        text_hex = COLOR_MAP.get(self.text_var.get(), "#000000")
        
        config = {
            "bg": bg_hex,
            "text": text_hex,
            "theme": self.theme_var.get()
        }
        self.apply_callback(config)
        self.window.destroy()