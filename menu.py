from enum import Enum
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QMessageBox
import game
from PyQt5.QtCore import Qt


class Map(Enum):
    empty = "пол.png"
    coin = "монета.png"
    wall = "wall.jpg"
    fin = "finish.png"

# Визначення рівня 0
lvl0 = [
    # Карта рівня
    [Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall],
    [Map.wall, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.wall],
    [Map.wall, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.wall],
    [Map.wall, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.wall],
    [Map.wall, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.wall],
    [Map.wall, Map.empty, Map.empty, Map.coin, Map.empty, Map.coin, Map.empty, Map.coin, Map.empty, Map.fin, Map.empty, Map.empty, Map.empty, Map.wall],
    [Map.wall, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.wall],
    [Map.wall, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.wall],
    [Map.wall, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.wall],
    [Map.wall, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.wall],
    [Map.wall, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.wall],
    [Map.wall, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.wall],
    [Map.wall, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.empty, Map.wall],
    [Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall],
]

# Визначення рівня 1
lvl1 = [
    # Карта рівня
    [Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall],
    [Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall],
    [Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall],
    [Map.wall, Map.wall, Map.wall, Map.empty, Map.fin, Map.empty, Map.empty, Map.empty, Map.coin, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall],
    [Map.wall, Map.wall, Map.wall, Map.empty, Map.wall, Map.wall, Map.wall, Map.wall, Map.empty, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall],
    [Map.wall, Map.wall, Map.wall, Map.empty, Map.wall, Map.wall, Map.wall, Map.wall, Map.empty, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall],
    [Map.wall, Map.wall, Map.wall, Map.empty, Map.wall, Map.wall, Map.wall, Map.wall, Map.empty, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall],
    [Map.wall, Map.wall, Map.wall, Map.empty, Map.wall, Map.wall, Map.wall, Map.wall, Map.empty, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall],
    [Map.wall, Map.wall, Map.wall, Map.empty, Map.wall, Map.wall, Map.wall, Map.wall, Map.empty, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall],
    [Map.wall, Map.wall, Map.wall, Map.empty, Map.wall, Map.wall, Map.wall, Map.wall, Map.coin, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall],
    [Map.wall, Map.wall, Map.wall, Map.empty, Map.empty, Map.coin, Map.empty, Map.empty, Map.empty, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall],
    [Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall],
    [Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall],
    [Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall, Map.wall],
]

# Клас основного віджета гри
class Menu(QWidget):
    def __init__(self):
        super().__init__()

        # Основний вертикальний layout
        main_layout = QVBoxLayout()
        label_menu = QLabel("Меню")  # Заголовок меню
        layout1 = QHBoxLayout()  # Горизонтальні layout'и для кнопок
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()
        layout4 = QHBoxLayout()
        main_layout.addWidget(label_menu, alignment=Qt.AlignCenter | Qt.AlignTop)

        main_layout.addLayout(layout4)

        # Створення кнопок для рівнів
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

        # Додавання кнопок до горизонтальних layout'ів
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
        # layout4.addWidget(buttonlang)  # Додати кнопку мови при необхідності

        main_layout.addLayout(layout1)
        main_layout.addLayout(layout2)
        main_layout.addLayout(layout3)

        # Прив'язка подій до кнопок
        buttontest.clicked.connect(self.test)
        button1.clicked.connect(self.lvl1)
        self.setLayout(main_layout)

    # Метод, який викликається при натисканні кнопки "test"
    def test(self):
        # Створення інформаційного вікна
        info = QMessageBox()
        info.setText("Для завершення рівня потрібно дійти до фінішу, монетки не обов'язкові. Керування циклом відбувається на праву кнопку миші")
        info.exec()
        self.hide()  # Приховування основного вікна

        Game = game.Game()  # Ініціалізація гри
        Game.drawmap(lvl0, 670, 50)  # Відображення карти рівня
        while Game.p:
            Game.loop()  # Основний ігровий цикл

        self.show()  # Показ основного вікна після завершення гри

    # Метод, який викликається при натисканні кнопки "lvl 1"
    def lvl1(self):
        # Створення інформаційного вікна
        info = QMessageBox()
        info.setText("Для завершення рівня потрібно дійти до фінішу, монетки не обов'язкові. Керування циклом відбувається на праву кнопку миші")
        info.exec()
        self.hide()  # Приховування основного вікна

        Game = game.Game()  # Ініціалізація гри
        Game.drawmap(lvl1, 770, 150)  # Відображення карти рівня
        while Game.p:
            Game.loop()  # Основний ігровий цикл

        self.show()  # Показ основного вікна після завершення гри

    # Перевизначення методу resizeEvent
    def resizeEvent(self, event):
        print("1")  # Виведення повідомлення при зміні розміру вікна

    # Перевизначення методу closeEvent
    def closeEvent(self, e):
        QWidget.closeEvent(self, e)  # Виклик базового методу закриття вікна

# Функція запуску додатку
def start():
    pass

app = QApplication([])  # Ініціалізація додатку
w = Menu()  # Створення віджета гри
w.show()  # Показ віджета
app.exec_()  # Запуск основного циклу додатку
