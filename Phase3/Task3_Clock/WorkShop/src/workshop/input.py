from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton
)
from PySide6.QtCore import Signal
from PySide6.QtGui import QIntValidator


class Input(QWidget):
    time_entered = Signal(int, int, int)

    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

        self._hour_input = QLineEdit()
        self._min_input = QLineEdit()
        self._sec_input = QLineEdit()

        self._hour_input.setPlaceholderText("Hour")
        self._min_input.setPlaceholderText("Minute")
        self._sec_input.setPlaceholderText("Second")

        self._hour_input.setValidator(QIntValidator(0, 11))
        self._min_input.setValidator(QIntValidator(0, 59))
        self._sec_input.setValidator(QIntValidator(0, 59))

        self._confirm_button = QPushButton("Confirm")
        self._confirm_button.clicked.connect(self._confirm_input)

        input_layout = QHBoxLayout()
        input_layout.addWidget(self._hour_input)
        input_layout.addWidget(self._min_input)
        input_layout.addWidget(self._sec_input)

        layout = QVBoxLayout(self)
        layout.addLayout(input_layout)
        layout.addWidget(self._confirm_button)

    def _confirm_input(self):
        hour = int(self._hour_input.text())
        minute = int(self._min_input.text())
        second = int(self._sec_input.text())

        self.time_entered.emit(hour, minute, second)