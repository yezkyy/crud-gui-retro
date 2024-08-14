# CRUD GUI Project

This is a simple yet interactive CRUD (Create, Read, Update, Delete) application built with Python. The project uses Tkinter for the graphical user interface (GUI) and SQLite for the database, making it easy to manage and interact with your data.

## Folder Structure

The project is organized as follows:

```bash
Project/
│
├── app/
│ ├── init.py # Initializes the app module.
│ ├── crud_operations.py # Core CRUD functions.
│
├── gui/
│ ├── init.py # Initializes the GUI module.
│ ├── forms.py # Manages form dialogs for CRUD operations.
│ ├── theme.py # Applies the retro visual theme.
│ ├── buttons.py # Handles button creation and styling.
│
├── main.py # The main entry point for the application.
└── README.md # Project overview and instructions.
```

### Explanation of Folders and Files

- **`app/`:** Contains the core logic for the application.
  - `crud_operations.py`: Implements the CRUD operations using SQLite.

- **`gui/`:** Handles the graphical user interface components.
  - `forms.py`: Manages form input dialogs for creating and updating items.
  - `theme.py`: Contains functions to apply the retro theme across the GUI.
  - `buttons.py`: Manages the creation and styling of buttons.

- **`main.py`:** The main script that initializes the GUI, applies the theme, and connects to the CRUD operations.

## Setup

To set up and run the application locally, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/repo-name.git
   cd repo-name
   ```
2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```
   
3. **Run the Application**

   ```bash
   python main.py
   ```
