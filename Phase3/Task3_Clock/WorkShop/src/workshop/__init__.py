from PySide6.QtWidgets import QApplication

from workshop.window import Window


def main() -> None:
    print("Hello from workshop!")

    app = QApplication()
    window = Window()

    app.exec()