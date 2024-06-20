import random
import pygame
from pygame.locals import QUIT, USEREVENT, MOUSEBUTTONDOWN
import time
# розмір екрана гри
gamewin = (1320, 700)
game_ower =False
# Класс для створення прямокутників (хітбоксів)
class Area():
  def __init__(self, mw, x, y, width, height, color, function =lambda:None, pic=None):
      self.rect = pygame.Rect(x, y, width, height) #прямоугольник
      self.fill_color = color
      self.mw = mw
      self.function = function
      self.pic = pic

  # метод для зміни кольорів
  def color(self, new_color):
      self.fill_color = new_color

  # метод для зафарбовування прямокутника
  def fill(self):
      pygame.draw.rect(self.mw, self.fill_color, self.rect)

  # створення контура
  def outline(self, frame_color, thickness): #обводка существующего прямоугольника
      pygame.draw.rect(self.mw, frame_color, self.rect, thickness)

  # перевірка натискання мишкою
  def collidepoint(self, x, y):
      return self.rect.collidepoint(x, y)

  #перевірка дотику інших прямокутників
  def colliderect(self, rect):
      return self.rect.colliderect(rect)

  # відображення картинок у прямокутнику
  def drawpic(self):
      #self.rect = self.obj.get_rect()
      self.mw.blit(self.obj, (self.rect.x, self.rect.y))

  #встановлення картинки для прямокутника
  def setpic(self,pic,widht=50,height=50):
      self.pic = pic
      self.obj = pygame.transform.scale(pygame.image.load(self.pic), (widht, height))

# класс для створення надписів
class Label(Area):
  def set_text(self, text, fsize=12, text_color=(0, 0, 0),):
      self.text = text

      self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

  def draw(self, shift_x=0, shift_y=0):
      #self.fill()
      try:
        self.drawpic()
      except:
          pass
      self.mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

# класс для створення кнопки циклу
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


        self.button_whiletxt.draw(35,7)
        self.button_whileup.draw(5,5)
        self.button_whiledown.draw(5,5)

# класс для обробки циклів створених гравцем
class Cycle():
    def __init__(self, buttons, iters):
        self.iters = iters
        self.res = self.parse(buttons)
    def function(self):
        for j in range(self.iters):
            for i in self.res:
                if not(game_ower):
                    i.function()

    def parse(self, buttons):
        res = []

        for i in buttons:
            if i.text == "repeat":
                x = Cycle(buttons, i.count)
                res.append(x)

            elif i.text == "  end":
                return res
            else:
                res.append(i)
        return res

# основний ігровий класс
class Game():
    # метод для відображення рівнів
    def drawmap(self, lvl, x=0,y=0):
        self.player = Area(self.screen, x, y, 50, 50, None, lambda: None, )
        self.player.setpic("роботправо.png")
        self.x = x
        self.y = y
        x,y = self.background_middle.topright
        for row in lvl:
            for block in row:
                objfloor = Area(self.screen, x, y, 50, 50, None, lambda: None, )
                objfloor.setpic("пол.png")
                self.map.append(objfloor)
                if block.value == "finish.png":
                    self.fin = Area(self.screen, x, y, 50, 50, None, lambda: None, )
                    self.fin.setpic("finish.png")
                    x += 50
                    continue
                obj = Area(self.screen, x, y, 50, 50, None, lambda: None, )
                obj.setpic(block.value)
                if block.value == "монета.png":
                    self.monee.append(obj)
                elif block.value == "wall.jpg":
                    self.wall.append(obj)

                x+=50
            x=self.background_middle.topright[0]
            y+=50
        self.map.append(self.player)

    # ініціалізація основних параметрів гри
    def __init__(self):
        self.p = True
        pygame.display.init()
        pygame.font.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(gamewin)
        self.money = 0
        #self.background = pygame.transform.scale(pygame.image.load("сетка.png"), (700, 700))

        self.background_left = self.rect = pygame.Rect(0, 0, 120, gamewin[1])
        self.background_middle = self.rect = pygame.Rect(120, 0, 500, gamewin[1])
        # self.player = pygame.transform.scale(pygame.image.load("право.png"), (50, 50))
        #
        # self.player = Area(self.screen,620,100,50,50,None,lambda: None,)
        # self.player.setpic("право.png")
        # self.wall = Area(self.screen,720,100,50,50,None,lambda: None,)
        # self.wall.setpic("wall.jpg")
        # self.fin = Area(self.screen,720,150,50,50,None,lambda :None,)
        # self.fin.setpic("finish.png")
        #
        # self.floor = Area(self.screen,720,50,50,50,None,lambda :None,)
        # self.floor.setpic("пол.png")
        # self.map =[self.wall,self.fin,self.floor,self.player]
        #
        # self.mone = Area(self.screen, 670, 150, 50, 50, None, lambda: None, )
        # self.mone.setpic("монета.png")


        self.direction = 90

        self.startbtn = Label(self.screen, 325, 0, 100, 30, (255, 0, 0), self.start)
        self.startbtn.setpic("оранжевый.png",100,30)
        self.startbtn.set_text("  start")

        self.button_forward = Label(self.screen,10,0,100,30,None,self.forward,)
        self.button_forward.set_text("forward")
        self.button_forward.setpic("зелёный.png",100,30)

        self.button_right = Label(self.screen,10,55,100,30,(255,0,0),self.rotate)
        self.button_right.set_text("  right")
        self.button_right.setpic("оранжевый.png", 100, 30)

        self.button_left = Label(self.screen,10,110,100,30,(255,0,0),self.rotate)
        self.button_left.set_text("  left")

        self.button_left.setpic("оранжевый.png", 100, 30)

        self.button_while = Label(self.screen, 10, 165, 100, 30, (255, 0, 0))
        self.button_while.set_text("repeat")
        self.button_while.setpic("фиолетовый.png", 100, 30)

        self.button_whiletxt = Label(self.screen, self.button_while.rect.x+40, self.button_while.rect.y, 10, 10, self.button_while.fill_color )
        self.button_whiletxt.set_text("1")

        self.button_whileup = Label(self.screen, self.button_while.rect.x+80, self.button_while.rect.y, 20, 30, (255, 250, 0))
        self.button_whileup.set_text("+")

        self.button_whiledown = Label(self.screen, self.button_while.rect.x, self.button_while.rect.y, 20, 30, (255, 250, 0)  )
        self.button_whiledown.set_text("−")

        self.button_end = Label(self.screen, 10, 220, 100, 30, (255, 0, 0) )
        self.button_end.set_text("  end")
        self.button_end.setpic("фиолетовый.png",100,30)

        self.button_clear = Label(self.screen, 10, gamewin[1]-50, 100, 30, (255, 0, 0), self.clear)
        self.button_clear.set_text("clear")
        self.button_clear.setpic("синий.png",100,30)


        self.moving = False
        self.movingobj = None
        self.buttons =[self.button_forward,self.button_right,self.button_left,self.button_while,self.button_end,self.button_whiletxt, self.button_clear]
        self.buttonswhile =[self.button_whileup,self.button_whiledown]
        self.additional_buttons = [self.startbtn]
        self.monee = []
        self.map = []
        self.wall =[]

    # основний ігровий цикл
    def loop(self):
        # перевірка натискання кнопки закриття гри
        for event in pygame.event.get():
            if event.type == QUIT:
                self.p = False
                #pygame.quit()


            if event.type == MOUSEBUTTONDOWN and event.button == 3:
                x,y = event.pos
                for button in self.additional_buttons:
                    if button.__class__.__name__ == "Whilebut":
                        if button.button_whileup.collidepoint(x, y):
                            button.button_whileup.function()
                        elif button.button_whiledown.collidepoint(x, y):
                            button.button_whiledown.function()

            if event.type == MOUSEBUTTONDOWN and event.button ==1:
                x, y = event.pos
                if self.button_forward.collidepoint(x, y):
                    button_fw = Label(self.screen, 0, 0, 100, 30, (255, 0, 0), self.forward)
                    button_fw.set_text("forward")
                    button_fw.setpic("зелёный.png",100,30)
                    self.additional_buttons.append(button_fw)

                elif self.button_right.collidepoint(x, y):
                    button_r = Label(self.screen, 0, 55, 100, 30, (255, 0, 0), lambda: self.rotate(90))
                    button_r.set_text("  right")
                    button_r.setpic("оранжевый.png",100,30)
                    self.additional_buttons.append(button_r)

                elif self.button_left.collidepoint(x, y):
                    button_l = Label(self.screen, 0, 110, 100, 30, (255, 0, 0), lambda: self.rotate(-90))
                    button_l.set_text("  left")
                    button_l.setpic("оранжевый.png", 100, 30)
                    self.additional_buttons.append(button_l)

                elif self.startbtn.collidepoint(x,y):
                    self.start()

                elif self.button_while.collidepoint(x,y):
                    button_while = Whilebut(self.screen, 10, 165, 100, 30, (255, 0, 0), lambda: None)
                    button_while.set_text("repeat")
                    button_while.setpic("фиолетовый.png", 100, 30)
                    self.additional_buttons.append(button_while)


                elif self.button_end.collidepoint(x,y):
                    button_end = Label(self.screen, 10, 220, 100, 30, (255, 0, 0), lambda: None)
                    button_end.set_text("  end")
                    button_end.setpic("фиолетовый.png", 100, 30)

                    self.additional_buttons.append(button_end)
                elif self.button_clear.collidepoint(x,y):
                    self.button_clear.function()


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

    def clear(self):
        self.additional_buttons =[self.startbtn]
    def update(self):

        pygame.draw.rect(self.screen,(30,33,36),self.background_middle)

        for button in self.additional_buttons:
            button.draw(30,7)

        #self.screen.blit(self.background, (620, 0))

        pygame.draw.rect(self.screen, (56, 69, 73), self.background_left)

        for button in self.buttons:
            button.draw(30,7)
        for button in self.buttonswhile:
            button.draw(5, 5)
        #self.screen.blit(self.player, (self.rect.x, self.rect.y))
        for obj in self.map:
            obj.drawpic()
        for obj in self.wall:
            obj.drawpic()
        for money in self.monee:
            money.drawpic()

        self.fin.drawpic()
        self.player.drawpic()

        self.clock.tick(40)
        pygame.display.update()

    def check(self):
        for obj in self.wall:
            if self.player.colliderect(obj):
                self.player.rect.x = self.x
                self.player.rect.y = self.y
                message =["Спробуй знову","Ти можеш краще","Давай ще раз",]
                self.show_message(message[random.randint(0,2)])
                time.sleep(2)  # Задержка на 2 секунды
                self.update()  # Обновляем экран, чтобы убрать сообщение
                self.direction = 0
                self.rotate(90)
                return True

        if self.player.colliderect(self.fin) and self.go:
            self.show_message("Win money "+str(self.money))
            time.sleep(2)  # Задержка на 2 секунды
            self.player.rect.x = self.x
            self.player.rect.y = self.y
            self.direction = 0
            self.rotate(90)
            self.update()  # Обновляем экран, чтобы убрать сообщение

            return True
        for money in self.monee:
            if len(self.monee )!=0 and self.player.colliderect(money):
                self.money+=1
                self.monee.remove(money)
                del money
        if not(self.player.colliderect(self.fin)) and self.go:
            self.player.rect.x = self.x
            self.player.rect.y = self.y
            message = ["Спробуй знову", "Ти можеш краще", "Давай ще раз", ]
            self.show_message(message[random.randint(0, 2)])
            time.sleep(2)  # Задержка на 2 секунды
            self.update()  # Обновляем экран, чтобы убрать сообщение
            self.direction = 0
            self.rotate(90)
    def show_message(self, text):
        # Создаём поверхность с сообщением
        font = pygame.font.SysFont('verdana', 50)
        message = font.render(text, True, (255, 0, 0))  # Красный текст
        text_rect = message.get_rect(center=(gamewin[0] / 2-250, gamewin[1] / 2))

        # Определяем размеры и позицию прямоугольника для фона
        padding = 20  # Отступы вокруг текста
        background_rect = pygame.Rect(
            text_rect.left - padding,
            text_rect.top - padding,
            text_rect.width + 2 * padding,
            text_rect.height + 2 * padding
        )

        # Рисуем прямоугольник с фоном
        background_color = (255, 255, 255)  # Черный цвет фона
        pygame.draw.rect(self.screen, background_color, background_rect)

        # Отображаем текст поверх прямоугольника
        self.screen.blit(message, text_rect)
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
        self.go = False
        algoritm =  self.conectblock()

        x = Cycle(iter(algoritm),1)
        x.function()
        self.go = True
        self.check()


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
            self.player.rect.x += x
            self.player.rect.y += y
            self.update()
        self.check()
        time.sleep(0.3)
    def rotate(self,direction ):
        self.direction += direction
        if self.direction % 360 == 90:
            #self.player = pygame.transform.scale(pygame.image.load("право.png"), (50, 50))
            self.player.setpic("роботправо.png")
        elif self.direction % 360 == 180:
            #self.player = pygame.transform.scale(pygame.image.load("низ.png"), (50, 50))
            self.player.setpic("роботниз.png")
        elif self.direction % 360 == 270:
            #self.player = pygame.transform.scale(pygame.image.load("лево.png"), (50, 50))
            self.player.setpic("роботлево.png")
        elif self.direction % 360 == 0:
            #self.player = pygame.transform.scale(pygame.image.load("верх.png"), (50, 50))
            self.player.setpic("роботверх.png")
        self.update()

#
# Game = Game()
#
# while True:
#     Game.loop()