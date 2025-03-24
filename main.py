import sys
from src.TextEditor import TextEditor
from PyQt5.QtWidgets import QApplication
from src.utils import setup_logger

logger = setup_logger(__name__)

def main():
    try:
        app = QApplication(sys.argv)
        
        logger.info("Запуск текстового редактора")
        editor = TextEditor()
        editor.show()
        
        sys.exit(app.exec_())
    except Exception as e:
        logger.error(f"Ошибка при запуске приложения: {e}")
        raise

if __name__ == "__main__":
    main()
