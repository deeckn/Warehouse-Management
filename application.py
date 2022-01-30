import sys
from PySide6.QtWidgets import QApplication


class Application:
    def __init__(self) -> None:
        self.app = QApplication(sys.argv)

        self.current_view = None  # <-- Change this to your view class
        self.current_controller = None

    def start(self):
        # self.current_view.show() <-- Uncomment this to run for view testing
        sys.exit(self.app.exec())
