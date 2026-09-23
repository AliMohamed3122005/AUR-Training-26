from PySide6.QtCore import QObject, Property, Signal, QTimer


class MyData(QObject):
    hours_changed = Signal()
    mins_changed = Signal()
    secs_changed = Signal()

    def __init__(self, parent: QObject | None = None):
        super().__init__(parent)

        self._hours = 0
        self._mins = 0
        self._secs = 0

        self._timer = QTimer(self)
        self._timer.timeout.connect(self._increment)
        self._timer.start(1000)

    @Property(int, notify=hours_changed)
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, new: int):
        if self._hours != new:
            self._hours = new
            self.hours_changed.emit()

    @Property(int, notify=mins_changed)
    def mins(self):
        return self._mins

    @mins.setter
    def mins(self, new: int):
        if self._mins != new:
            self._mins = new
            self.mins_changed.emit()

    @Property(int, notify=secs_changed)
    def secs(self):
        return self._secs

    @secs.setter
    def secs(self, new: int):
        if self._secs != new:
            self._secs = new
            self.secs_changed.emit()

    def _increment(self):
        self.secs += 1

        if self.secs >= 60:
            self.secs = 0
            self.mins += 1

        if self.mins >= 60:
            self.mins = 0
            self.hours += 1

        if self.hours >= 12:
            self.hours = 0