# Python Typing Speed Test

A modern desktop typing speed test application built with Python and Tkinter, featuring real-time typing analytics, dynamic theme customization, and a modular architecture.

## Features

- Random paragraph generation from a local text pool
- Real-time WPM (Words Per Minute) calculation
- Live accuracy tracking
- Elapsed time monitoring
- Safe metric calculations protected against division-by-zero crashes
- Dedicated settings window for UI customization
- Multiple built-in themes:
  - Default (Vibrant Orange)
  - Dark Mode (Slate Charcoal)
  - Light Mode
  - Sci-Fi Theme (Neon-inspired)
- Live theme synchronization across dropdown menus
- Read-only comboboxes to prevent invalid user input
- Modular callback-based architecture for clean communication between files

---

## Technologies Used

- Python 3
- Tkinter
- TTK (Tile Toolkit)

---

## Project Structure

```text
Python-Typing-Speed-Test/
│
├── main.py          # Main application logic and UI
├── settings.py      # Theme and customization manager
├── text.txt         # Paragraph/text database
└── README.md        # Project documentation
```

---

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/Naveebpk123/Python-Typing-Speed-Test.git
```

### 2. Navigate Into the Project Folder

```bash
cd Python-Typing-Speed-Test
```

### 3. Run the Application

```bash
python main.py
```

---

## How It Works

### Parent → Child Callback Architecture

When the settings window is opened, `main.py` passes a callback function into `settings.py`.

After the user applies changes, the settings module sends the selected configuration back to the main application through the callback system. This keeps the architecture modular while avoiding circular imports and unnecessary global dependencies.

---

## Metrics System

The application continuously tracks:

- Typing speed (WPM)
- Accuracy percentage
- Elapsed time

All calculations are safely guarded against invalid states and runtime crashes.

---

## Future Improvements

- Add a live countdown timer mode
- Save local high scores and statistics
- Add difficulty modes with advanced vocabulary pools

---

## Author

Created by Naveeb Pacheerikkuth

GitHub: https://github.com/Naveebpk123
