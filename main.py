import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
QApplication.setHighDpiScaleFactorRoundingPolicy(
    Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
)

from src.ui.MainWindowController import MainWindowController
def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    main_window = MainWindowController()
    main_window.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()