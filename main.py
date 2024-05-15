import pygame
from pygame.locals import QUIT, USEREVENT, MOUSEBUTTONDOWN
from pygame.event import Event, post
from random import randint

from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QSpinBox, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPainter, QPixmap



class Game():
    def __init__(self):
        pygame.display.init()
        self.screen = pygame.display.set_mode((400, 400), pygame.HIDDEN)
        self.r = 1
        self.v = 1
        self.pos = 10, 10

    def loop(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        pygame.display.update()




class GameWidget(QWidget):
    def __init__(self):
        super().__init__()
        main_layout = QHBoxLayout()
        self.game = Game()
        self.timer = QTimer()
        self.timer.timeout.connect(self.pygame_loop)
        self.timer.start(40)

    def pygame_loop(self):
        self.game.loop()
        self.update(0, 0, 400, 400)

    def on_box(self, val):
        #post(Event(USEREVENT, {'v': val}))
        pass
    def paintEvent(self, e):
        if self.game:
            buf = self.game.screen.get_buffer()
            img = QImage(buf, 400, 400, QImage.Format_RGB32)
            p = QPainter(self)
            p.drawImage(100, 0, img)

    def resizeEvent(self, event):

        print("resize")



    def closeEvent(self, e):
        QWidget.closeEvent(self, e)
        post(Event(QUIT))


if __name__ == "__main__":
    import sys
    #print(sys.argv)
    app = QApplication([])
    w = GameWidget()
    w.resize(500, 400)
    w.show()
    app.exec_()