# ⌨️ Keystroke Logger Toolkit

> A Python-based GUI application for monitoring and analyzing keyboard events (Pressed, Held, Released) in real time.

---

## 📌 Overview

**Keystroke Logger Toolkit** is a desktop application built using **Tkinter** and **pynput** that demonstrates real-time keyboard event handling and logging.

This project focuses on:

- Event-driven programming
- GUI development using Tkinter
- File handling with JSON and text formats

It provides a simple interface to start capturing keyboard activity and stores it in structured and readable formats.

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **GUI Framework:** Tkinter
- **Keyboard Listener:** pynput
- **Data Storage:** JSON, TXT

---

## ✨ Features

- ✅ GUI-based control to start monitoring
- ✅ Tracks key states:
  - Pressed
  - Held
  - Released

- ✅ Dual logging system:
  - `logs.json` → structured event logs
  - `logs.txt` → continuous keystroke stream

- ✅ Real-time event capturing
- ✅ Lightweight and easy to run

---

## 📂 Project Structure

```bash
Keystroke-Logger-Toolkit/
│── keylogger.py     # Main application (GUI + logic)
│── logs.json        # Stores structured key events
│── logs.txt         # Stores continuous keystrokes
│── README.md        # Documentation
│── LICENSE          # MIT License
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/himanshusalunke-works/Keystroke-Logger-Toolkit.git
cd Keystroke-Logger-Toolkit
```

### 2. Install dependencies

```bash
pip install pynput
```

---

## ▶️ Usage

1. Run the application:

```bash
python keylogger.py
```

2. Click **"Start"** in the GUI

3. Press keys to monitor events

4. Check generated files:
   - `logs.json` → detailed event logs
   - `logs.txt` → readable keystroke sequence

---

## 📊 How It Works

### 🔹 Event Handling

- `on_press()`
  → Detects key press and hold behavior

- `on_release()`
  → Detects key release and updates logs

---

### 🔹 Logging System

- **JSON File (`logs.json`)**

```json
[{ "Pressed": "Key.a" }, { "Held": "Key.a" }, { "Released": "Key.a" }]
```

- **Text File (`logs.txt`)**

```
Key.aKey.bKey.c
```

---

## ⚠️ Ethical & Legal Disclaimer

This project is intended **strictly for educational and demonstration purposes**.

- Do **not** use this software for:
  - Unauthorized monitoring
  - Collecting sensitive or personal data

- Always obtain **explicit user consent** before running the application

Misuse of this software may violate privacy laws and regulations.

---

## 🚀 Future Improvements

- 🔹 Add Start/Stop toggle functionality
- 🔹 Improve human-readable key formatting
- 🔹 Filter special/system keys (Shift, Ctrl, etc.)
- 🔹 Add in-app log viewer
- 🔹 Export logs to CSV format
- 🔹 Optimize repeated "Held" event logging

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👤 Author

**Himanshu**

- GitHub: [https://github.com/himanshusalunke-works](https://github.com/himanshusalunke-works)

---

## ⭐ Support

If you found this project useful:

- ⭐ Star the repository
- 🍴 Fork it
- 🛠️ Contribute improvements
