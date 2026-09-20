from PySide6.QtWidgets import QHBoxLayout, QPushButton, QWidget
from PySide6.QtCore import Signal


class Buttons(QWidget):
    start = Signal()
    pause = Signal()
    reset = Signal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self._start_button=QPushButton("Start")
        self._reset_button=QPushButton("Reset")

        self._layout=QHBoxLayout(self)
        self._layout.addWidget(self._start_button)
        self._layout.addWidget(self._reset_button)

        self._start_button.clicked.connect(self._b1_clicked)
        self._reset_button.clicked.connect(self._b2_clicked)

        self._timer_paused = True

    @property
    def timer_paused(self) -> bool:
        return self._timer_paused
    @timer_paused.setter
    def timer_paused(self,state:bool) ->None:
        self._timer_paused = state
        if state:
            self._start_button.setText("Start")
        else:
            self._start_button.setText("Pause")
    def _b1_clicked(self) -> None:
        if self._timer_paused:
            self.start.emit()
            self.timer_paused = False
        else:
            self.pause.emit()
            self.timer_paused = True
    def _b2_clicked(self)->None:
        self.reset.emit()