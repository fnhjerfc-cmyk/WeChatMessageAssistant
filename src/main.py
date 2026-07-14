import sys

from PySide6.QtWidgets import QApplication

from views.main_window import MainWindow
from controllers.main_controller import MainController


app = QApplication(sys.argv)

window = MainWindow()

controller = MainController(window)

window.show()

sys.exit(app.exec())