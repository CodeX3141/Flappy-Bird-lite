import os
from random import randint
import game
import tkinter as tk
from tkinter import messagebox
import datetime
from datetime import datetime



os.environ['pygame_HIDE_SUPPORT_PROMPT'] = "hide"

from pygame.sprite import Sprite
import pygame

import sys  

f = 4/5

root = tk.Tk()
w = int(root.winfo_screenwidth() * f)
h = int(root.winfo_screenheight() * f)




window = pygame.display.set_mode((w,h))
pygame.init()


image = pygame.image.load(r'wallpaper2.jpg')
image = pygame.transform.scale(image, (w,h)) 


pygame.display.set_caption('square run')
programIcon = pygame.image.load('spaceship.png')
pygame.display.set_caption('Square run')

pygame.display.set_icon(programIcon)

pygame.mixer.music.load(os.path.join(os.getcwd(),'overture.mp3'))
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)



myfont = pygame.font.SysFont("Agency FB", 20)


def possibility(num):
    if randint(1,num) == int(num/2):
        return True
    else :
        return False

class coin(pygame.sprite.Sprite):
  
    image = pygame.image.load(r'spaceship.png')
  
    rect = pygame.Rect(0,0,0,0)
    def __init__(self,color,width,height):
        super().__init__()
        self.image = pygame.image.load(r'spaceship.png')
        self.image = pygame.transform.scale(self.image, (width,height))
        #self.image.set_colorkey(color)
        
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect.x + int(width/2),self.rect.y + int(height/2))
        pygame.draw.rect(window,color,self.rect,10)


def rnInt(x):
    if possibility(x):
        return 1
    else:
        return 0

class bodies():

     rint2 = randint(100,150)
     rect = pygame.Rect(0,0,0,0)
     rect2 = pygame.Rect(0,0,0,0)
     coin = pygame.Rect(0,0,0,0)
     rint = 0
     i = 0
     shader = pygame.Rect(0,0,0,0)
     power = pygame.Rect(0,0,0,0)
     
     def __init__(self):
          

          xxxx = 0
     
     
     
     
     def draw(self,xPos,rInt,color,gap,coinY,powerH): 
          shaderH = 30
          self.i += 1
          fli = 75
          
          
          coinH = 15
          yellow = (255,255,0)
          xPos2 = xPos - 125
          
          shaderPos = int((shaderH - coinH)/2)
          
          self.coin = pygame.Rect(xPos2,rInt + coinY,coinH,coinH)
          self.shader = pygame.Rect(xPos2 - shaderPos,rInt + coinY - shaderPos,shaderH,shaderH)
          self.power = pygame.Rect(xPos2 - shaderPos,rInt + coinY,powerH,powerH)
          
          self.rect = pygame.Rect(xPos,-1000,50,rInt + 1000)
          self.rect2 = pygame.Rect(xPos,rInt + gap,50,h - rInt - gap + 100)
          

          pygame.draw.rect(window,color,self.rect,rnInt(fli) )
          pygame.draw.rect(window,color,self.rect2,rnInt(fli))
          
          
          
          if powerH != 0:
              if possibility(5):
                    pygame.draw.rect(window,(255,0,0),self.power)
          else:
                pygame.draw.rect(window,yellow,self.coin)
          if possibility(10):
                pygame.draw.rect(window,randomColor(),self.shader)
      
     def collide(self,rect):
        return self.rect.colliderect(rect) or self.rect2.colliderect(rect)
     
     def collideCoin(self,rect):
        return self.coin.colliderect(rect)
        
     def collidePower(self,rect):
        return self.power.colliderect(rect)
     def destroyCoin(self):
        self.coin = pygame.Rect(0,0,0,0)

def nothing():
 gdhsghdfgwshdgwidgi = 0

def gameOver(ee,score):
 pygame.mixer.Channel(0).play(pygame.mixer.Sound('death.mp3'), maxtime=600)
 pygame.mixer.Channel(0).set_volume(0.2)
 pygame.time.wait(2500)
 
 
 
 main()
 


def complete():
 print('You have completed this game')
 
 
 
def randomColor():
    return (randint(0,255),randint(0,255),randint(0,255))


def main():
 hP = 50
 hc = 10
 hc2 = 10
 score = 0
 
 clock = pygame.time.Clock()

 #window = pygame.display.set_mode((w,h))
 

 

 


 running = True

 movement = 1

 x = 100
 y = h/2

 imgW = hP
 imgH = 70

 

 color = (255,255,0)

 Img = pygame.image.load('spaceship.png')
 Img = pygame.transform.scale(Img, (imgW,imgW))
 
 POWERUPS = 3
 LIFES = 500
 i = 0

 sure = True

 #bull = bullet()
 gp = 225
 pill = bodies()
 height = []
 color = []
 coinHeights = []
 powerUps = []
 powerPos = []
 wave = 400
 XPOS = w
 fps = 1000
 
 
 

 while running:
  sidec = (255,0,255)
  b = pygame.Rect(x + hP,y + hP,hc,hc)
  
  
  b2 = pygame.Rect(x-hc,y + hP,hc,hc)
  
  
  b3 = pygame.Rect(x + hP,y-hc,hc,hc)
  
  
  
  b4 = pygame.Rect(x-hc,y-hc,hc,hc)
  
  
  t = pygame.Rect( x + hP/2 - hc/2,y + hP/2 - hc/2,hc,hc)
  
  
  t1 = pygame.Rect( x + hP/2 - hc2/2,y - hc2,hc2,hc2)
  t2 = pygame.Rect( x - hc2,y + hP/2 - hc2/2,hc2,hc2)
  t3 = pygame.Rect( x + hP/2 - hc2/2,y + hP,hc2,hc2)
  t4 = pygame.Rect( x + hP,y + hP/2 - hc2/2,hc2,hc2)
  
  
  
  
  now = datetime.now()
  time = now.strftime("%H:%M:%S")
  #bull.shoot(x,y)
  score = int(i)
  
  
  if i < wave/4:
   gp -= 0
  elif i >= wave/4 and i < 2*wave/4:
   gp -= 25
  elif i >= 2*wave/4 and i < 3*wave/4:
   gp -= 50
  else:
   gp -= 75
 
  break1 = 0
 
  
 
  if len(height) == 0 or XPOS == break1:
  
   for dd in range(wave):
    color.append((randint(0,255),randint(0,255),randint(0,255)))
    height.append(randint(1,h-250))
    coinHeights.append(randint(0,gp))
    if possibility(45):
        powerUps.append(30)
        powerPos.append(randint(1,h-20))
    else:
        powerUps.append(0)
        powerPos.append(0)
    
 
  key = pygame.key.get_pressed()
  for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONUP:
          i += 5
          POWERUPS -= 1
          if POWERUPS >= 0:
           x,y = pygame.mouse.get_pos()
          
      if event.type == pygame.QUIT:
          running = False
      if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_w :
              y -= 2*movement + 1
           
      '''if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            bull = Bullet(x,y,imgRect)
            #bull.update()'''
	
  
	
  
  side_ways = 2

  if y == 0 + hc or y == h - hc:
   if LIFES > 0:
    
   
    pygame.mixer.Channel(1).play(pygame.mixer.Sound('damage.mp3'), maxtime=600)
    pygame.mixer.Channel(1).set_volume(0.2)
    fps = 1
    LIFES -= 1
    nothing()
   else :
    i = 0
    gameOver('lose',score)
    
  if key[pygame.K_SPACE] or key[pygame.K_w] or key[pygame.K_UP]:
   
   x1 = x
   y1 = y 
   y -= 2*movement + 1
   
   
  if key[pygame.K_s] or key[pygame.K_DOWN]:
   y += movement + 2
 
 
  if key[pygame.K_a] or key[pygame.K_LEFT]:
   x -= movement + side_ways
 	
    
  if key[pygame.K_d] or key[pygame.K_RIGHT]:
   x += movement + side_ways
  if key[pygame.K_x] and key[pygame.K_c]:
   exit()
  
  
  
  
 
 
  if x + hc > w:
   x = w - hc
  elif x < 0 + hc:
   x = 0 + hc
 
  elif y > h - hP - hc:
   y = h - hP - hc
  elif y < 0 + hc:
   y = 0 + hc
 	
  elif x == -(imgW + hc + hc) or y == -(imgW + hc + hc):
   x = 0
   y = 0
  
  
  window.blit(image, (0, 0))
  
  
  
  
  
  
  
  
  
  window.blit(Img,(x,y))
  imgRect = Img.get_rect()
  imgRect.center = (x+int(imgW/2),y+int(imgW/2))
  
 
  for ii in range(wave):
   pill.draw(XPOS + (ii * 270 ),int(height[ii] *(10/10)),color[ii],gp,coinHeights[ii],powerUps[ii])
   if pill.collidePower(imgRect) or pill.collidePower(b) or pill.collidePower(b2) or pill.collidePower(b3) or pill.collidePower(b4):
        LIFES = 500
   
   if pill.collide(imgRect) or pill.collide(b) or pill.collide(b2) or pill.collide(b3) or pill.collide(b4):
    fps = 1
    if LIFES > 0:
     
     pygame.mixer.Channel(1).play(pygame.mixer.Sound('damage.mp3'), maxtime=600)
     pygame.mixer.Channel(1).set_volume(0.2)
     
     LIFES -= 1
     
     nothing()
    
    else:
     i = 0
     gameOver(ii,score)
   else:
    fps = 1000
   if pill.collideCoin(imgRect) or pill.collideCoin(b) or pill.collideCoin(b2) or pill.collideCoin(b3) or pill.collideCoin(b4):
    if sure:
     i += 3/wave
     sure = True
    else:
     sure = False
    pill.destroyCoin()
  
  '''if pill.collide(imgRect):
   gameOver()'''
  
  pygame.draw.rect(window,(255,0,0),imgRect,3)
  
  pygame.draw.rect(window,randomColor(),b)
  pygame.draw.rect(window,randomColor(),b2)
  pygame.draw.rect(window,randomColor(),b3)
  pygame.draw.rect(window,randomColor(),b4)
  pygame.draw.rect(window,randomColor(),t)
  pygame.draw.rect(window,randomColor(),t1)
  pygame.draw.rect(window,randomColor(),t2)
  pygame.draw.rect(window,randomColor(),t3)
  pygame.draw.rect(window,randomColor(),t4)
 
  XPOS -= 1
  
  
  scorel = 'SCORE : ' + str(score)
  label = myfont.render(scorel, 1, (255,255,0))
  window.blit(label, (10, 10))
  
  clock.tick(fps)
  if POWERUPS >= 0:
   label2 = myfont.render("POWERUPS : " + str(POWERUPS), 1, (255,255,0))
  else:
   label2 = myfont.render("POWERUPS : 0", 1, (255,255,0))
  window.blit(label2,(w-100,10))
  
  if LIFES > 0:
   
   label3 = myfont.render("LIFES : " + str(int(LIFES/100)), 1, (255,255,0))
  else:
   label3 = myfont.render("LIFES : 0", 1, (255,255,0))
  window.blit(label3,(w-100,30))
  
  
  timeL = myfont.render('TIME : ' + time,1,(255,255,0))
  window.blit(timeL,(10,30))
 
  
  
  
  
  y += movement 
  
  if i > wave + 4.2:
   complete()
   
  pygame.display.flip()
 pygame.quit()
main()