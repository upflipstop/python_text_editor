from pathlib import Path

# Пути к директориям
ROOT_DIR = Path(__file__).parent.parent
ASSETS_DIR = ROOT_DIR / 'assets'
ICONS_DIR = ASSETS_DIR / 'icons'

# Настройки окна
WINDOW_TITLE = "MyOwnTexteditor"
WINDOW_GEOMETRY = {
    'width': 1030,
    'height': 800,
    'x': 100,
    'y': 100
}

# Настройки редактора
EDITOR_SETTINGS = {
    'tab_width': 33,
    'font_size': 12,
    'default_font': 'Arial'
}

# Форматы файлов
FILE_FORMATS = {
    'writer': '*.writer',
    'all': '*.*'
}

# Горячие клавиши
SHORTCUTS = {
    'new': 'Ctrl+N',
    'open': 'Ctrl+O',
    'save': 'Ctrl+S',
    'print': 'Ctrl+P',
    'preview': 'Ctrl+Shift+P',
    'undo': 'Ctrl+Z',
    'redo': 'Ctrl+Shift+Z',
    'copy': 'Ctrl+C',
    'cut': 'Ctrl+X',
    'paste': 'Ctrl+V'
}

# Форматы даты и времени
DATE_TIME_FORMATS = [
    "%A, %d. %B %Y %H:%M",
    "%A, %d. %B %Y",
    "%d. %B %Y %H:%M",
    "%d.%m.%Y %H:%M",
    "%d. %B %Y",
    "%d %m %Y",
    "%d.%m.%Y",
    "%x",
    "%X",
    "%H:%M"
] 