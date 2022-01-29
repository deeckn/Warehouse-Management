import sys
from PySide6.QtWidgets import QApplication


class Application:
    def __init__(self) -> None:
        self.app = QApplication(sys.argv)

        """
        For the view developers
        Test your code through here, you only have to run main

        self.current_view = MyView() <-- Just change the class view object
        """
        self.current_view = None

    def start(self):
        # self.current_view.show() <-- Uncomment this to run
        sys.exit(self.app.exec())
