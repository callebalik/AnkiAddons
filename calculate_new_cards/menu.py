from aqt.qt import QAction

from .config import conf
from .gui.anking_menu import get_anking_menu


def setup_menu() -> None:
    menu = get_anking_menu()
    a = QAction("Calculate New Cards To Do", menu)
    menu.addAction(a)
    a.triggered.connect(lambda _: conf.open_config())


setup_menu()
