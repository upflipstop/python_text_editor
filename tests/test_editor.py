import pytest
from src.TextEditor import TextEditor
from PyQt5.QtWidgets import QApplication
import sys
from PyQt5.QtGui import QTextListFormat

@pytest.fixture
def app():
    """Фикстура для создания экземпляра QApplication"""
    app = QApplication(sys.argv)
    yield app
    app.quit()

@pytest.fixture
def editor(app):
    """Фикстура для создания экземпляра TextEditor"""
    return TextEditor()

def test_editor_init(editor):
    """Тест инициализации редактора"""
    assert editor.filename == ""
    assert editor.changes_saved == True

def test_new_file(editor):
    """Тест создания нового файла"""
    editor.new()
    assert editor.text.toPlainText() == ""

def test_save_changes_flag(editor):
    """Тест флага сохранения изменений"""

def test_window_geometry(editor):
    """Тест геометрии окна"""
    geometry = editor.geometry()
    assert geometry.width() == 1030
    assert geometry.height() == 800
    assert geometry.x() == 100
    assert geometry.y() == 100

def test_window_title(editor):
    """Тест заголовка окна"""
    assert editor.windowTitle() == "MyOwnTexteditor"

def test_tab_width(editor):
    """Тест ширины табуляции"""
    assert editor.text.tabStopWidth() == 33

def test_bullet_list(editor):
    """Тест создания маркированного списка"""
    editor.text.setText("Test")
    editor.bullet_list()
    cursor = editor.text.textCursor()
    current_list = cursor.currentList()
    assert current_list is not None
    assert current_list.format().style() == QTextListFormat.ListDisc

def test_number_list(editor):
    """Тест создания нумерованного списка"""
    editor.text.setText("Test")
    editor.number_list()
    cursor = editor.text.textCursor()
    current_list = cursor.currentList()
    assert current_list is not None
    assert current_list.format().style() == QTextListFormat.ListDecimal

def test_cursor_position(editor):
    """Тест позиции курсора"""
    editor.text.setText("Test\nText")
    cursor = editor.text.textCursor()
    cursor.setPosition(6)  # Перемещаем курсор на вторую строку
    editor.text.setTextCursor(cursor)
    editor.cursor_position()
    assert "Line: 2" in editor.statusbar.currentMessage()
  