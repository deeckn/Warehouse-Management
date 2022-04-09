from views.root_container import RootContainer
from PySide6.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = RootContainer()
    view.showFullScreen()
    sys.exit(app.exec())
