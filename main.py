from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Astrometry")
        button = QPushButton("woo")


        self.setCentralWidget(button)



app = QApplication([])

window = MainWindow()
window.show()

app.exec()


