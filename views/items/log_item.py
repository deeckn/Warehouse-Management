from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout
from PySide6.QtGui import QFont, Qt

class LogItem(QWidget):
    def __init__(self,date: str, time:str, txt: str):
        font = QFont("Poppins")
        font.setPixelSize(14)
        QWidget.__init__(self, None)
        self.setFont(font)
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.date_label = QLabel(date)
        self.date_label.setFixedHeight(21)
        self.time_label  = QLabel(time)
        self.time_label.setFixedHeight(21)
        self.event_label = QLabel(txt)
        self.event_label.setMinimumWidth(180)
        self.event_label.setWordWrap(True) # Able the label to be multi-line

        # Choose
        self.event_label.setAlignment(Qt.AlignLeft)
        #self.event_label.setAlignment(Qt.AlignCenter)

        # Add Labels to layout
        self.main_layout.addWidget(self.date_label)
        self.main_layout.addWidget(self.time_label)
        self.main_layout.addWidget(self.event_label)