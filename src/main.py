import sys

from PySide6.QtWidgets import QApplication

from src.views.main_window import MainWindow
from src.controllers.main_controller import MainController


app = QApplication(sys.argv)

window = MainWindow()

controller = MainController(window)


def main():
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()