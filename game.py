import pygame
from pygame.locals import QUIT, USEREVENT, MOUSEBUTTONDOWN
from pygame.event import Event, post
from random import randint

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
        self.screen = pygame.display.set_mode((gamewin[0], gamewin[1]))
        self.background = pygame.transform.scale(pygame.image.load("сетка.png"), (700, 700))
        self.player = pygame.transform.scale(pygame.image.load("право.png"), (50, 50))
        self.button = Label(self.screen,0,0,100,50,(255,0,0))
        self.button.set_text("Button")
        self.rect = self.player.get_rect()
        self.rect.x = 150
        self.rect.y = 0



    def loop(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        self.screen.blit(self.background, (150, 0))
        self.screen.blit(self.player, (self.rect.x, self.rect.y))
        self.button.draw(30,15)
        pygame.display.update()


    def forward(self):
        for i in range(50):
            self.rect.x += 1

Game = Game()

while True:
    Game.loop()