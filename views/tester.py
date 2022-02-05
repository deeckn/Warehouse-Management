from view import MyView
from PySide6.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = MyView()
    view.set_user_label("TESTER00")
    view.showFullScreen()
    sys.exit(app.exec_())