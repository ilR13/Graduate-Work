from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QLabel
import game
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPainter



class GameWidget(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()
        label_menu = QLabel("Меню")
        layout1 = QHBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()
        layout4 = QHBoxLayout()
        main_layout.addWidget(label_menu,alignment=Qt.AlignCenter|Qt.AlignTop )


        main_layout.addLayout(layout4)

        button1 = QPushButton("lvl 1")
        button2 = QPushButton("lvl 2")
        button3 = QPushButton("lvl 3")
        button4 = QPushButton("lvl 4")
        button5 = QPushButton("lvl 5")
        button6 = QPushButton("lvl 6")
        button7 = QPushButton("lvl 7")
        button8 = QPushButton("lvl 8")
        button9 = QPushButton("lvl 9")

        buttontest = QPushButton("test")
        buttonlang = QPushButton("Language")

        layout1.addWidget(button1)
        layout1.addWidget(button2)
        layout1.addWidget(button3)
        layout2.addWidget(button4)
        layout2.addWidget(button5)
        layout2.addWidget(button6)
        layout3.addWidget(button7)
        layout3.addWidget(button8)
        layout3.addWidget(button9)

        layout4.addWidget(buttontest)
        layout4.addWidget(buttonlang)


        main_layout.addLayout(layout1)
        main_layout.addLayout(layout2)
        main_layout.addLayout(layout3)
        buttontest.clicked.connect(self.test)
        self.setLayout(main_layout)
    def test(self):
        #self.closeEvent()
        self.hide()
        Game = game.Game()

        while True:
            Game.loop()




    def resizeEvent(self, event):
        print("1")

    def closeEvent(self, e):
        QWidget.closeEvent(self, e)




def start():
    pass

app = QApplication([])
w = GameWidget()
#w.resize (5000, 500)
w.show()
app.exec_()