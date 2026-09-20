from PySide6.QtWidgets import QStackedWidget, QLineEdit, QLabel,QWidget
from PySide6.QtGui import QIntValidator
from PySide6.QtCore import QTimer, Signal, Qt


class Stack(QStackedWidget):
    time_stopped = Signal(bool)
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self._input = QLineEdit()
        self._input.setPlaceholderText("Enter time in seconds")
        self._input.setValidator(QIntValidator(1,99999999,self))
        self._timer_label = QLabel("00:00")
        self._timer_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.addWidget(self._input)
        self.addWidget(self._timer_label)
        self._timer = QTimer(self)
        self._timer.setInterval(1000)
        self._timer.timeout.connect(self._decrement)
        self._remaining_seconds = 0
    def start_counter(self) -> None:
        if self.currentIndex() == 0:
            value = self._input.text()
            if not value:
                return
            self._remaining_seconds=int(value)
            self._timer_label.setText(
                f"{self._remaining_seconds // 60:02d}:"
                f"{self._remaining_seconds % 60:02d}"
            )
            self.setCurrentIndex(1)
        self._timer.start()
        self.time_stopped.emit(False)
    def _decrement(self) -> None:
        self._remaining_seconds -=1
        minutes = self._remaining_seconds // 60
        seconds = self._remaining_seconds % 60
        self._timer_label.setText(f"{minutes:02d}:{seconds:02d}")
        if self._remaining_seconds <=0:
            self._timer.stop()
            self.reset()
    def reset(self) ->None:
        self._remaining_seconds=0
        self._timer_label.setText("00:00")

        self._input.clear()
        self.setCurrentIndex(0)

        self.time_stopped.emit(True)
    def pause(self) -> None:
        self._timer.stop()
        self.time_stopped.emit(True)