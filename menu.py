from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QLabel

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPainter



class GameWidget(QWidget):
    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout()
        label_menu = QLabel("Меню")
        main_layout.addWidget(label_menu,alignment=Qt.AlignCenter|Qt.AlignTop )
        control_layout = QHBoxLayout()
        control_button = QPushButton("Control")
        # control_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        control_layout.addWidget(control_button)
        main_layout.addLayout(control_layout)
        control_button.clicked.connect(self.start)
        self.setLayout(main_layout)
    def start(self):
        app.quit()



    def resizeEvent(self, event):
        print("resize")

    def closeEvent(self, e):
        QWidget.closeEvent(self, e)





app = QApplication([])
w = GameWidget()
w.resize (500, 500)
w.show()
app.exec_()