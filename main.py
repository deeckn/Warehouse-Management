from application import Application
import sys
from PySide6.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    application = Application()
    application.start()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
