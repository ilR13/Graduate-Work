import pygame
from pygame.locals import QUIT, USEREVENT, MOUSEBUTTONDOWN
from pygame.event import Event, post
from random import randint
import time
gamewin = (1320, 700)

class Area():
  def __init__(self, mw, x, y, width, height, color, function):
      self.rect = pygame.Rect(x, y, width, height) #прямоугольник
      self.fill_color = color
      self.mw = mw
      self.function = function
  def color(self, new_color):
      self.fill_color = new_color
  def fill(self):
      pygame.draw.rect(self.mw, self.fill_color, self.rect)
  def outline(self, frame_color, thickness): #обводка существующего прямоугольника
      pygame.draw.rect(self.mw, frame_color, self.rect, thickness)
  def collidepoint(self, x, y):
      return self.rect.collidepoint(x, y)

  def colliderect(self, rect):
      return self.rect.colliderect(rect)
'''класс надпись'''
class Label(Area):
  def set_text(self, text, fsize=12, text_color=(0, 0, 0),):
      self.text = text

      self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

  def draw(self, shift_x=0, shift_y=0):
      self.fill()
      self.mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


class Whilebut(Label):
    def __init__(self, mw, x, y, width, height, color, function,):
        super().__init__( mw, x, y, width, height, color, function)
        self.count = 1
        self.button_whiletxt = Label(self.mw, x + 35, y, 10, 10,color, None, )
        self.button_whiletxt.set_text("1")

        self.button_whileup = Label(self.mw, x + 80, y, 20, 30,(255, 250, 0), self.plus, )
        self.button_whileup.set_text("+")

        self.button_whiledown = Label(self.mw, x, y, 20,30, (255, 250, 0), self.minus, )
        self.button_whiledown.set_text("−")

    def plus(self):
        self.count +=1
        self.button_whiletxt.set_text(str(self.count))
    def minus(self):
        self.count -=1
        if self.count <=0:
            self.count = 1
        self.button_whiletxt.set_text(str(self.count))
    def draw(self, shift_x=0, shift_y=0):
        super().draw(shift_x,shift_y)

        self.button_whiletxt.rect.x = self.rect.x + 35
        self.button_whiletxt.rect.y = self.rect.y
        self.button_whileup.rect.x = self.rect.x + 80
        self.button_whileup.rect.y = self.rect.y
        self.button_whiledown.rect.x = self.rect.x
        self.button_whiledown.rect.y = self.rect.y


        self.button_whiletxt.draw(30,7)
        self.button_whileup.draw(5,5)
        self.button_whiledown.draw(5,5)

class Cycle():
    def __init__(self, buttons, iters):
        self.iters = iters
        self.res = self.parse(buttons)
    def function(self):
        for j in range(self.iters):
            for i in self.res:
                i.function()
    def parse(self, buttons):
        res = []

        for i in buttons:
            if i.text == "while":
                x = Cycle(buttons, i.count)
                res.append(x)

            elif i.text == "  end":
                return res
            else:
                res.append(i)


        return res
class Game():
    def __init__(self):
        pygame.display.init()
        pygame.font.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(gamewin)
        self.background = pygame.transform.scale(pygame.image.load("сетка.png"), (700, 700))

        self.background_left = self.rect = pygame.Rect(0, 0, 120, gamewin[1])
        self.background_middle = self.rect = pygame.Rect(120, 0, 500, gamewin[1])
        self.player = pygame.transform.scale(pygame.image.load("право.png"), (50, 50))
        self.direction = 90

        self.startbtn = Label(self.screen, 325, 0, 100, 30, (255, 0, 0), self.start)
        self.startbtn.set_text("  start")

        self.button_forward = Label(self.screen,10,0,100,30,(255,0,0),self.forward)
        self.button_forward.set_text("forward")
        self.button_right = Label(self.screen,10,55,100,30,(255,0,0),self.rotate)
        self.button_right.set_text("  right")
        self.button_left = Label(self.screen,10,110,100,30,(255,0,0),self.rotate)
        self.button_left.set_text("  left")


        self.button_while = Label(self.screen, 10, 165, 100, 30, (255, 0, 0), None)
        self.button_while.set_text("while")

        self.button_whiletxt = Label(self.screen, self.button_while.rect.x+35, self.button_while.rect.y, 10, 10, self.button_while.fill_color, None, )
        self.button_whiletxt.set_text("1")

        self.button_whileup = Label(self.screen, self.button_while.rect.x+80, self.button_while.rect.y, 20, 30, (255, 250, 0),  None,)
        self.button_whileup.set_text("+")

        self.button_whiledown = Label(self.screen, self.button_while.rect.x, self.button_while.rect.y, 20, 30, (255, 250, 0),  None,)
        self.button_whiledown.set_text("−")

        self.button_end = Label(self.screen, 10, 220, 100, 30, (255, 0, 0), None)
        self.button_end.set_text("  end")


        self.rect = self.player.get_rect()
        self.rect.x = 620
        self.rect.y = 100
        self.moving = False
        self.movingobj = None
        self.buttons =[self.button_forward,self.button_right,self.button_left,self.button_while,self.button_end,self.button_whiletxt]
        self.buttonswhile =[self.button_whileup,self.button_whiledown]
        self.additional_buttons = [self.startbtn]


    def loop(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 3:
                x,y = event.pos
                for button in self.additional_buttons:
                    if button.__class__.__name__ == "Whilebut":
                        if button.button_whileup.collidepoint(x,y):
                            button.button_whileup.function()
                        elif button.button_whiledown.collidepoint(x,y):
                            button.button_whiledown.function()

            if event.type == MOUSEBUTTONDOWN and event.button ==1:
                x, y = event.pos
                if self.button_forward.collidepoint(x, y):
                    button_fw = Label(self.screen, 0, 0, 100, 30, (255, 0, 0), self.forward)
                    button_fw.set_text("forward")
                    self.additional_buttons.append(button_fw)

                elif self.button_right.collidepoint(x, y):
                    button_r = Label(self.screen, 0, 55, 100, 30, (255, 0, 0), lambda: self.rotate(90))
                    button_r.set_text("  right")
                    self.additional_buttons.append(button_r)

                elif self.button_left.collidepoint(x, y):
                    button_l = Label(self.screen, 0, 110, 100, 30, (255, 0, 0), lambda: self.rotate(-90))
                    button_l.set_text("  left")
                    self.additional_buttons.append(button_l)

                elif self.startbtn.collidepoint(x,y):
                    self.start()

                elif self.button_while.collidepoint(x,y):
                    button_while = Whilebut(self.screen, 10, 165, 100, 30, (255, 0, 0), lambda: None)
                    button_while.set_text("while")
                    self.additional_buttons.append(button_while)

                elif self.button_end.collidepoint(x,y):
                    button_end = Label(self.screen, 10, 220, 100, 30, (255, 0, 0), lambda: None)
                    button_end.set_text("  end")
                    self.additional_buttons.append(button_end)

                for button in self.additional_buttons:
                    if button != self.startbtn:
                        if button.collidepoint(x,y):
                            self.moving = True
                            self.movingobj = button
                            break
            if event.type == pygame.MOUSEMOTION:
                if self.moving:
                    if not(self.movingobj == self.startbtn):
                        x_new, y_new = event.rel
                        self.movingobj.rect.x = self.movingobj.rect.x + x_new
                        self.movingobj.rect.y = self.movingobj.rect.y + y_new
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:

                for button in self.additional_buttons:
                    if not(button.colliderect(self.background_middle)):
                        self.additional_buttons.remove(button)
                        del button
                if self.moving:
                    buttons =[]
                    buttons.append(self.startbtn)
                    buttons.extend(self.conectblock())
                    for i in buttons:
                        if self.movingobj.colliderect(i):
                            button=buttons[-1]
                            self.movingobj.rect.x = button.rect.x
                            self.movingobj.rect.y = button.rect.bottom

                self.moving = False

        self.update()
    def wloop (self):
        pass



    def update(self):

        pygame.draw.rect(self.screen,(0,255,0),self.background_middle)

        for button in self.additional_buttons:
            button.draw(30,7)
        self.additional_buttons[0].outline((0,0,0),5)
        self.screen.blit(self.background, (620, 0))

        pygame.draw.rect(self.screen, (0, 0, 255), self.background_left)

        for button in self.buttons:
            button.draw(30,7)
        for button in self.buttonswhile:
            button.draw(5, 5)
        self.screen.blit(self.player, (self.rect.x, self.rect.y))
        self.clock.tick(40)
        pygame.display.update()

    def conectblock(self):
        algoritm = []
        block1 = self.additional_buttons[0]
        for i in range(len(self.additional_buttons)):
            flag = True
            for block2 in self.additional_buttons:
                if block1.rect.bottom == block2.rect.top:
                    algoritm.append(block2)
                    block1 = self.additional_buttons[self.additional_buttons.index(block2)]
                    flag = False
            if flag:
                return algoritm
        return  algoritm
    def start(self):
        algoritm =  self.conectblock()
        # i=0
        # while i <len(algoritm):
        #     if algoritm[i].text == "while":
        #         x = Cycle(algoritm[i + 1:], algoritm[i].count)
        #         i += len(x.res)
        #         x.function()
        #     print(algoritm[i].text)
        #     algoritm[i].function()
        #     i+=1
        x = Cycle(iter(algoritm),1)
        x.function()

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