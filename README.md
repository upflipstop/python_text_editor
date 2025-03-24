# Text Editor 📝

<div align="center">

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![PyQt5](https://img.shields.io/badge/PyQt5-5.15.10-green.svg)
![Tests](https://img.shields.io/badge/tests-pytest-yellow.svg)

*Powerful text editor with rich formatting capabilities built with PyQt5*

[Features](#-features) • [Installation](#-installation) • [Testing](#-testing) • [Project Structure](#-project-structure) • [Available Functions](#-available-functions) • [Architecture](#-architecture)

</div>

## 📋 About Project
Text Editor is a versatile software application designed for efficient text editing and formatting. Built with PyQt5, it provides a rich set of features for both basic text manipulation and advanced formatting options.

## ✨ Features

### Core Functionality
- 📂 **File Operations**
  - Create new files
  - Open existing files
  - Save changes
  - Print documents

### Text Editing
- ⚡ **Advanced Navigation**
  - Arrow key navigation
  - Word-by-word movement
  - Start/end line jumps
  
- 📝 **Text Manipulation**
  - Line/word deletion
  - Copy, cut, and paste
  - Undo/redo actions
  
- 🔍 **Search & Replace**
  - Text search functionality
  - Replace operation
  - Find and replace all

### Formatting Tools
- 🎨 **Text Formatting**
  - Font selection
  - Font size adjustment
  - Font color
  - Background color
  - Bold
  - Italic
  - Underline
  - Strikethrough

- 📊 **Document Elements**
  - Bullet lists
  - Numbered lists
  - Tables
  - Image insertion
  
- 🛠 **Additional Tools**
  - Date/time insertion
  - Counter
  - Page preview
  - Print functionality

## 🚀 Installation

### Quick Start
```bash
# Clone the repository
git clone https://github.com/upflipstop/mipt_python_projects.git
cd mipt_python_projects

# Run installation script
chmod +x run.sh
./run.sh
```

### Manual Installation
```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # For Unix/macOS
# or
.\venv\Scripts\activate  # For Windows

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

## 🧪 Testing

### Running Tests
```bash
# Install test dependencies
pip install pytest pytest-cov pytest-qt

# Run tests with coverage report
python -m pytest --cov=src tests/ --cov-report=html
```

### Test Coverage
- Unit tests cover core functionality
- Integration tests for UI components
- Test coverage report available in `htmlcov/` directory

## 🔧 Requirements
- Python 3.8 or higher
- PyQt5 5.15.10
- pytest (for testing)
- pytest-cov (for coverage reports)
- pytest-qt (for Qt testing)

## 📁 Project Structure
```
mipt_python_projects/
├── assets/
│   ├── icons/             # Application icons
│   └── screenshots/       # Screenshots for documentation
├── logs/                  # Log files
├── src/
│   ├── ext/               # Extensions
│   ├── utils/             # Utility functions
│   │   ├── __init__.py
│   │   └── logger.py      # Logging configuration
│   ├── constants.py       # Global constants
│   ├── Lexic.py           # Text formatting
│   ├── MenuBar.py         # Menu functionality
│   ├── TextEditor.py      # Main editor class
│   └── ToolBar.py         # Toolbar functionality
├── tests/
│   ├── __init__.py
│   ├── conftest.py        # Test configurations
│   └── test_editor.py     # Editor tests
├── main.py                # Entry point
├── requirements.txt       # Dependencies
└── run.sh                 # Installation script
```

## 🎯 Available Functions

### File Operations
1. [New File](assets/screenshots/new_file.png) - Create new file
2. [Open File](assets/screenshots/open_file.png) - Open existing file
3. [Save](assets/screenshots/save.png) - Save file

### Edit Operations
4. [Undo](assets/screenshots/action_back.png) - Undo last action
5. [Redo](assets/screenshots/action_forward.png) - Redo last action
6. [Copy](assets/screenshots/copy.png) - Copy selected text
7. [Cut](assets/screenshots/cut.png) - Cut selected text
8. [Paste](assets/screenshots/paste.png) - Paste copied text

### Formatting
9. [Fonts](assets/screenshots/fonts.png) - Select font
10. [Font Size](assets/screenshots/font_size.png) - Change font size
11. [Font Color](assets/screenshots/font_color.png) - Change font color
12. [Background Color](assets/screenshots/background_color.png) - Change text background
13. [Bold](assets/screenshots/bold.png) - Make text bold
14. [Italic](assets/screenshots/italic.png) - Make text italic
15. [Underline](assets/screenshots/underline.png) - Underline text
16. [Strikethrough](assets/screenshots/cross_out.png) - Strikethrough text

### Insert Elements
17. [Bullet List](assets/screenshots/bullet_list.png) - Create bullet list
18. [Numbered List](assets/screenshots/numbered_list.png) - Create numbered list
19. [Table](assets/screenshots/table.png) - Insert table
20. [Image](assets/screenshots/insert_image.png) - Insert image

### Additional Tools
21. [Find and Replace](assets/screenshots/find_and_replace.png) - Find and replace text
22. [Current Time](assets/screenshots/current_data_time.png) - Insert current date and time
23. [Counter](assets/screenshots/counter.png) - Add counter
24. [Page View](assets/screenshots/page_view.png) - Preview page
25. [Print](assets/screenshots/print.png) - Print document

## 📝 Logging

The application uses a structured logging system:

- Log files are stored in the `logs/` directory
- Supports different log levels: `INFO`, `ERROR`, `DEBUG`
- Each log entry includes a timestamp and contextual information for easier debugging

## 🛠️ Architecture

### `TextEditor` Class

- **Attributes:**
  - `filename`: Current file path
  - `changes_saved`: File modification status
  - `text`: Main text editing widget

- **Methods:**
  - `init_ui()`: Initialize user interface
  - `new()`: Create new file
  - `open()`: Open existing file
  - `save()`: Save current file
  - `preview()`: Preview document
  - `print()`: Print document
  - `bullet_list()`: Create bullet list
  - `number_list()`: Create numbered list
  - `cursor_position()`: Update cursor position

## 👥 Contributing

We welcome contributions from the community! To contribute, please follow these steps:

1. **Fork** the repository
2. **Create a new branch** for your feature or bugfix (`git checkout -b feature/improvement`)
3. **Make your changes** and add appropriate tests
4. **Run tests** to ensure everything works (`pytest`)
5. **Commit your changes** (`git commit -am 'Add new feature'`)
6. **Push to your branch** (`git push origin feature/improvement`)
7. **Create a Pull Request** for your changes to be reviewed

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
