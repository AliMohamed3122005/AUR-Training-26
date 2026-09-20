from PySide6.QtWidgets import QApplication
from task_6.window import Window
import sys


def main() -> None:
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    app.exec()