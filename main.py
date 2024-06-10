import pygame
from pygame.locals import QUIT, USEREVENT, MOUSEBUTTONDOWN
from pygame.event import Event, post
from random import randint

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPainter

gamewin = (700, 700)


class Game():
    def __init__(self):
        pygame.display.init()
        self.screen = pygame.display.set_mode((gamewin[0], gamewin[1]), pygame.HIDDEN)
        self.background = pygame.transform.scale(pygame.image.load("сетка.png"), (gamewin[0], gamewin[1]))
        self.player = pygame.transform.scale(pygame.image.load("право.png"), (50, 50))

        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.player.get_rect()
        self.rect.x = 0
        self.rect.y = 0


    def loop(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.player, (self.rect.x, self.rect.y))


    def forward(self):
        for i in range(50):
            self.rect.x += 1

class GameWidget(QWidget):
    def __init__(self):
        super().__init__()
        main_layout = QHBoxLayout()

        # Левая панель с элементами управления
        control_layout1 = QVBoxLayout()
        control_layout = QHBoxLayout()
        control_button = QPushButton("Control")
        control_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        control_layout.addWidget(control_button)
        control_layout.addStretch()  # Добавляем растяжку, чтобы кнопка была вверху
        control_layout1.addLayout(control_layout)
        main_layout.addLayout(control_layout1)



        # Инициализация игры
        self.game = Game()
        control_button.clicked.connect(self.game.forward)
        # Правильное обновление окна Pygame
        self.timer = QTimer()
        self.timer.timeout.connect(self.pygame_loop)
        self.timer.start(40)

        self.setLayout(main_layout)
        self.setMinimumSize(gamewin[0] + 105, gamewin[1])  # Увеличение ширины для панели управления

    def pygame_loop(self):
        self.game.loop()
        self.update(105, 0, gamewin[0], gamewin[1])  # Обновление окна Pygame

    def paintEvent(self, e):
        if self.game:
            buf = self.game.screen.get_buffer()
            img = QImage(buf, gamewin[0], gamewin[1], QImage.Format_RGB32)
            p = QPainter(self)
            p.drawImage(105, 0, img)  # Рисуем изображение со сдвигом

    def resizeEvent(self, event):
        print("resize")

    def closeEvent(self, e):
        QWidget.closeEvent(self, e)
        post(Event(QUIT))


if __name__ == "__main__":
    import sys

    app = QApplication([])
    w = GameWidget()
    w.show()
    app.exec_()
