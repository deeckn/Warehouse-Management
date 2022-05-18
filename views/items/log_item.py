from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout
from PySide6.QtGui import Qt
from views.theme import Theme
from data.orm.schema import Log


class LogItem(QWidget):
    def __init__(self, log_entry: Log):
        QWidget.__init__(self, None)

        main_layout = QHBoxLayout(self)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)

        date_label = QLabel(log_entry.get_date().replace("_", "/"))
        time_label = QLabel(log_entry.get_time().replace("_", ":"))
        event_label = QLabel(log_entry.get_description())

        for label in (date_label, time_label, event_label):
            label.setStyleSheet("background-color: none;")
            label.setFont(Theme.POPPINS_REGULAR_14)

        date_label.setFixedHeight(21)
        date_label.setMinimumWidth(110)
        time_label.setFixedHeight(21)
        time_label.setMinimumWidth(90)
        event_label.setMinimumWidth(180)
        event_label.setWordWrap(True)  # Able the label to be multi-line

        # Choose
        event_label.setAlignment(Qt.AlignLeft)

        # Add Labels to layout
        main_layout.addWidget(date_label)
        main_layout.addWidget(time_label)
        main_layout.addWidget(event_label)
