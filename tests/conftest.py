import pytest
import sys
from PyQt5.QtWidgets import QApplication

@pytest.fixture(scope="session")
def qapp():
    """
    Фикстура для создания единого экземпляра QApplication на всю сессию тестирования
    """
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    yield app 