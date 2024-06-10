import pygame
from pygame.locals import QUIT, USEREVENT, MOUSEBUTTONDOWN
from pygame.event import Event, post
from random import randint
import time
gamewin = (850, 700)

class Area():
  def __init__(self, mw, x=0, y=0, width=10, height=10, color=None):
      self.rect = pygame.Rect(x, y, width, height) #прямоугольник
      self.fill_color = color
      self.mw = mw
  def color(self, new_color):
      self.fill_color = new_color
  def fill(self):
      pygame.draw.rect(self.mw, self.fill_color, self.rect)
  def outline(self, frame_color, thickness): #обводка существующего прямоугольника
      pygame.draw.rect(self.mw, frame_color, self.rect, thickness)
  def collidepoint(self, x, y):
      return self.rect.collidepoint(x, y)
'''класс надпись'''
class Label(Area):
  def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
      self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
  def draw(self, shift_x=0, shift_y=0):
      self.fill()
      self.mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))



class Game():
    def __init__(self):
        pygame.display.init()
        pygame.font.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((gamewin[0], gamewin[1]))
        self.background = pygame.transform.scale(pygame.image.load("сетка.png"), (700, 700))
        self.background_left = self.rect = pygame.Rect(0, 0, 150, gamewin[1])
        self.player = pygame.transform.scale(pygame.image.load("право.png"), (50, 50))
        self.direction = 90
        self.button_forward = Label(self.screen,0,0,100,50,(255,0,0))
        self.button_forward.set_text("forward")
        self.button_right = Label(self.screen,0,55,100,50,(255,0,0))
        self.button_right.set_text("right")
        self.button_left = Label(self.screen,0,110,100,50,(255,0,0))
        self.button_left.set_text("left")
        self.rect = self.player.get_rect()
        self.rect.x = 150
        self.rect.y = 0
        self.moving = False

    def loop(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN and event.button ==1:
                x, y = event.pos
                if self.button_forward.collidepoint(x, y):
                    #self.forward()
                    self.moving = True
                    #del self.button_forward
                elif self.button_right.collidepoint(x, y):
                    self.rotate(90)
                elif self.button_left.collidepoint(x, y):
                    self.rotate(-90)

            if event.type == pygame.MOUSEMOTION:
                if self.moving:
                    x_new, y_new = event.rel
                    self.button_forward.rect.x = self.button_forward.rect.x + x_new
                    self.button_forward.rect.y = self.button_forward.rect.y + y_new
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.moving = False
        self.update()

    def update(self):
        self.screen.blit(self.background, (150, 0))
        pygame.draw.rect(self.screen, (0,0,255), self.background_left)
        self.screen.blit(self.player, (self.rect.x, self.rect.y))
        self.button_forward.draw(30, 15)
        self.button_left.draw(30, 15)
        self.button_right.draw(30, 15)
        self.clock.tick(40)
        pygame.display.update()

    def forward(self):
        if self.direction % 360 == 90:
            x = 1
            y = 0
        elif self.direction % 360 == 180:
            x = 0
            y = 1
        elif self.direction % 360 == 270:
            x = -1
            y = 0
        elif self.direction % 360 == 0:
            x = 0
            y = -1
        for i in range(50):
            self.rect.x += x
            self.rect.y += y
            self.update()
        time.sleep(0.3)
    def rotate(self,direction ):
        self.direction += direction
        if self.direction % 360 == 90:
            self.player = pygame.transform.scale(pygame.image.load("право.png"), (50, 50))
        elif self.direction % 360 == 180:
            self.player = pygame.transform.scale(pygame.image.load("низ.png"), (50, 50))
        elif self.direction % 360 == 270:
            self.player = pygame.transform.scale(pygame.image.load("лево.png"), (50, 50))
        elif self.direction % 360 == 0:
            self.player = pygame.transform.scale(pygame.image.load("верх.png"), (50, 50))
        self.update()

Game = Game()

while True:
    Game.loop()