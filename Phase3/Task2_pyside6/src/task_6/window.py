from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from task_6.buttons import Buttons
from task_6.stack import Stack

class Window(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self._central_widget=QWidget()
        self.setCentralWidget(self._central_widget)
        self._layout = QVBoxLayout(self._central_widget)

        self._buttons = Buttons()
        self._stack = Stack()

        self._layout.addWidget(self._stack)
        self._layout.addWidget(self._buttons)

        self._buttons.start.connect(self._stack.start_counter)
        self._buttons.pause.connect(self._stack.pause)
        self._buttons.reset.connect(self._stack.reset)

        self._stack.time_stopped.connect(self._switch_buttons)

    def _switch_buttons(self,state: bool)->None:
        self._buttons.timer_paused= state
