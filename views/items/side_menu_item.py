from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtGui import QFont, QColor, QPainter, QPixmap, QMouseEvent

"""
img = {
    "home",
    "user",
    "product",
    "notification",
    "goto",
    "fix",
    "files",
    "docs",
    "search",
    "logout"
}
"""


class SideMenuItem(QWidget):
    def __init__(self, img_type: str, text: str) -> None:
        QWidget.__init__(self, None)
        self.function = None               # Keeping function that tides to the item
        self.img_type = img_type            # Keep which type of picture is the item
        self.setFixedSize(400, 74)
        self.setContentsMargins(38, 21, 0, 21)

        # Font
        font = QFont("Poppins")
        font.setPixelSize(24)
        font.setBold(True)

        # IMG
        img = QPixmap(f":/icons/{img_type}.svg").scaled(30, 30)
        self.paint(img, "#F8F8FF")  # paint the svg to ghost white
        self.img_label = QLabel(self)
        self.img_label.setPixmap(img)
        self.img_label.setGeometry(38, 21, 30, 30)

        # Text label
        self.text_label = QLabel(self)
        self.text_label.setText(text)
        self.text_label.setFont(font)
        self.text_label.setStyleSheet("color: #F8F8FF")
        self.text_label.setGeometry(74, 20, 322, 36)

    # Set a function when clicked
    def set_function(self, function) -> None:
        self.function = function

    # When click called the function
    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.function()

    # Add function with the original function
    # append to make function run after original function
    # insert to make function run before original function
    def add_function(self, function, add_type: str = "append") -> None:
        if self.function != None:
            temp = self.function
            if(add_type == "append"):
                def new():
                    temp()
                    function()
            elif (add_type == "insert"):
                def new():
                    function()
                    temp()
            self.function = new
        else:
            self.set_function(function)

    # UI
    def click(self) -> None:
        new_img = QPixmap(f":/icons/{self.img_type}.svg").scaled(30, 30)
        self.paint(new_img, "#FDCB6E")
        self.img_label.setPixmap(new_img)
        self.text_label.setStyleSheet("color: #FDCB6E")

    def unclick(self) -> None:
        new_img = QPixmap(f":/icons/{self.img_type}.svg").scaled(30, 30)
        self.paint(new_img, "#F8F8FF")
        self.img_label.setPixmap(new_img)
        self.text_label.setStyleSheet("color: #F8F8FF")

    def paint(self, img: QPixmap, color_code: str) -> None:
        painter = QPainter(img)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(img.rect(), QColor(color_code))
        painter.end()
