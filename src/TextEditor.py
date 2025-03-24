from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QIcon, QTextListFormat, QTextCharFormat, QFont, QTextCursor, QImage, QContextMenuEvent
from PyQt5.QtPrintSupport import QPrintPreviewDialog, QPrintDialog
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QFileDialog, QDialog, QFontComboBox, \
    QComboBox, QColorDialog, QMessageBox, QMenu, QSpinBox
from src.ext import *
from src.Lexic import Lexic
from src.MenuBar import MenuBar
from src.ToolBar import ToolBar
import logging

logging.basicConfig(
    filename='editor.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

class TextEditor(QMainWindow):
    """
    Основной класс текстового редактора.
    
    Attributes:
        filename (str): Путь к текущему файлу
        changes_saved (bool): Флаг сохранения изменений
    """

    def __init__(self):
        super().__init__()
        self.filename: str = ""
        self.changes_saved: bool = True
        self.init_ui()

    def init_ui(self):
        self.text = QTextEdit(self)

        self.text.setTabStopWidth(33)

        ToolBar.init_tool_bar(self)
        Lexic.init_format_bar(self)
        MenuBar.init_menu_bar(self)
        self.setCentralWidget(self.text)

        self.statusbar = self.statusBar()

        self.text.cursorPositionChanged.connect(self.cursor_position)

        self.text.setContextMenuPolicy(Qt.CustomContextMenu)
        self.text.customContextMenuRequested.connect(self.context)

        self.text.textChanged.connect(self.changed)

        self.setGeometry(100, 100, 1030, 800)
        self.setWindowTitle("MyOwnTexteditor")
        self.setWindowIcon(QIcon("assets/icons/icon.png"))

    @staticmethod
    def new():
        spawn = TextEditor()
        spawn.show()

    def open(self):
        try:
            filename = QFileDialog.getOpenFileName(self, 'Open File', ".", "(*.writer)")[0]
            if filename:
                with open(filename, "rt", encoding='utf-8') as file:
                    self.text.setText(file.read())
                    self.filename = filename
                    self.changes_saved = True
        except Exception as e:
            logger.error(f"Ошибка при открытии файла: {e}")
            QMessageBox.critical(self, "Ошибка", "Не удалось открыть файл")

    def save(self):
        try:
            if not self.filename:
                self.filename = QFileDialog.getSaveFileName(self, 'Save File')[0]

            if self.filename:

                if not self.filename.endswith(".writer"):
                    self.filename += ".writer"

                with open(self.filename, "wt") as file:
                    file.write(self.text.toHtml())

                self.changes_saved = True
                logger.info(f"Файл {self.filename} успешно сохранен")
        except Exception as e:
            logger.error(f"Ошибка при сохранении файла: {e}")
            raise

    def preview(self):

        preview = QPrintPreviewDialog()

        preview.paintRequested.connect(lambda p: self.text.print_(p))

        preview.exec_()

    def print(self):

        dialog = QPrintDialog()

        if dialog.exec_() == QDialog.Accepted:
            self.text.document().print_(dialog.printer())

    def bullet_list(self):

        cursor = self.text.textCursor()

        cursor.insertList(QTextListFormat.ListDisc)

    def number_list(self):

        cursor = self.text.textCursor()

        cursor.insertList(QTextListFormat.ListDecimal)

    def cursor_position(self):

        cursor = self.text.textCursor()

        line = cursor.blockNumber() + 1
        col = cursor.columnNumber()

        self.statusbar.showMessage("Line: {} | Column: {}".format(line, col))

    def insert_image(self):

        filename, _ = QFileDialog.getOpenFileName(self, 'Insert image', ".",
                                                  "Images (*.png *.xpm *.jpg *.bmp *.gif)")

        image = QImage(filename)

        if image.isNull():

            popup = QMessageBox(QMessageBox.Critical,
                                "Image load error",
                                "Could not load image file!",
                                QMessageBox.Ok,
                                self)
            popup.show()

        else:

            cursor = self.text.textCursor()

            cursor.insertImage(image, filename)

    def word_count(self):

        wc = wordcount.WordCount(self)

        wc.get_text()

        wc.show()

    def context(self, pos):

        cursor = self.text.textCursor()

        table = cursor.currentTable()
        if table:

            menu = QMenu(self)

            append_row_action = QAction("Append row", self)
            append_row_action.triggered.connect(lambda: table.appendRows(1))

            append_col_action = QAction("Append column", self)
            append_col_action.triggered.connect(lambda: table.appendColumns(1))

            remove_row_action = QAction("Remove row", self)
            remove_row_action.triggered.connect(self.remove_row)

            remove_col_action = QAction("Remove column", self)
            remove_col_action.triggered.connect(self.remove_col)

            insert_row_action = QAction("Insert row", self)
            insert_row_action.triggered.connect(self.insert_row)

            insert_col_action = QAction("Insert column", self)
            insert_col_action.triggered.connect(self.insert_col)

            merge_action = QAction("Merge cells", self)
            merge_action.triggered.connect(lambda: table.mergeCells(cursor))

            if not cursor.hasSelection():
                merge_action.setEnabled(False)

            split_action = QAction("Split cells", self)

            cell = table.cellAt(cursor)
            if cell.rowSpan() > 1 or cell.columnSpan() > 1:

                split_action.triggered.connect(lambda: table.splitCell(cell.row(), cell.column(), 1, 1))

            else:
                split_action.setEnabled(False)

            menu.addAction(append_row_action)
            menu.addAction(append_col_action)

            menu.addSeparator()

            menu.addAction(remove_row_action)
            menu.addAction(remove_col_action)

            menu.addSeparator()

            menu.addAction(insert_row_action)
            menu.addAction(insert_col_action)

            menu.addSeparator()

            menu.addAction(merge_action)
            menu.addAction(split_action)

            pos = self.mapToGlobal(pos)
            if self.toolbar.isVisible():
                pos.setY(pos.y() + 45)

            if self.formatbar.isVisible():
                pos.setY(pos.y() + 45)

            menu.move(pos)

            menu.show()

        else:

            event = QContextMenuEvent(QContextMenuEvent.Mouse, QPoint())

            self.text.contextMenuEvent(event)

    def remove_row(self):

        cursor = self.text.textCursor()

        table = cursor.currentTable()

        cell = table.cellAt(cursor)

        table.remove_rows(cell.row(), 1)

    def remove_col(self):

        cursor = self.text.textCursor()
        table = cursor.currentTable()

        cell = table.cellAt(cursor)

        table.remove_columns(cell.column(), 1)

    def insert_row(self):

        cursor = self.text.textCursor()

        table = cursor.currentTable()

        cell = table.cellAt(cursor)

        table.insert_rows(cell.row(), 1)

    def insert_col(self):

        cursor = self.text.textCursor()

        table = cursor.currentTable()

        cell = table.cellAt(cursor)

        table.insert_columns(cell.column(), 1)

    def changed(self):
        self.changes_saved = False

    def closeEvent(self, event):

        if self.changes_saved:
            event.accept()
        else:
            popup = QMessageBox(self)
            popup.setIcon(QMessageBox.Warning)
            popup.setText("The document has been modified")
            popup.setInformativeText("Do you want to save your changes?")
            popup.setStandardButtons(QMessageBox.Save |
                                     QMessageBox.Cancel |
                                     QMessageBox.Discard)
            popup.setDefaultButton(QMessageBox.Save)
            answer = popup.exec_()
            if answer == QMessageBox.Save:
                self.save()
                event.accept()
            elif answer == QMessageBox.Discard:
                event.accept()
            else:
                event.ignore()
