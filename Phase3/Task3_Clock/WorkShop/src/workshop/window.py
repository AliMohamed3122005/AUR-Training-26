from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout

from workshop.data import MyData
from workshop.status_widget import StatusWidget
from workshop.input import Input


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self._data = MyData()

        self._status = StatusWidget(
            "clock.qml",
            self._data
        )

        self._input = Input()

        self._input.time_entered.connect(self._set_time)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        layout.addWidget(self._status)
        layout.addWidget(self._input)

        self.setCentralWidget(central_widget)

        self.show()

    def _set_time(self, hour: int, min: int, sec: int):
        self._data.hours = hour
        self._data.mins = min
        self._data.secs = sec