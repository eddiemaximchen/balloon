#  Balloon base class and 3 subclasses

import pygame
import random
from pygame.locals import *
import pygwidgets
from abc import ABC, abstractmethod

N_BALLOONS=15
BALLOON_MISSED='Missed'
BALLOON_MOVING='Balloon Moving'

class Balloon(ABC):

    popSoundLoaded = False
    popSound = None  # load when first balloon is created

    @abstractmethod
    def __init__(self, window, maxWidth, maxHeight, ID,
                 objImage, size, nPoints, speedY):
        self.window = window
        self.ID = ID
        self.balloonImage = objImage
        self.size = size
        self.nPoints = nPoints
        self.speedY = speedY
        if not Balloon.popSoundLoaded:  # load first time only
            Balloon.popSoundLoaded = True
            Balloon.popSound = pygame.mixer.Sound('sounds/balloonPop.wav')

        balloonRect = self.balloonImage.getRect()
        self.width = balloonRect.width
        self.height = balloonRect.height
        # Position so balloon is within the width of the window,
        # but below the bottom
        self.x = random.randrange(maxWidth - self.width)
        self.y = maxHeight + random.randrange(75)
        self.balloonImage.setLoc((self.x, self.y))

    def clickedInside(self, mousePoint):
        myRect = pygame.Rect(self.x, self.y, self.width, self.height)
        if myRect.collidepoint(mousePoint):
            Balloon.popSound.play()
            return True, self.nPoints # True here means it was hit
        else:
            return False, 0  # not hit, no points

    def update(self):
        self.y = self.y - self.speedY   # update y position by speed
        self.balloonImage.setLoc((self.x, self.y))
        if self.y < -self.height:     # off the top of the window
            return BALLOON_MISSED
        else:
            return BALLOON_MOVING

    def draw(self):
        self.balloonImage.draw()

    def __del__(self):
        print(self.size, 'Balloon', self.ID,'is going away')
from pygame.locals import *
import random
import pygwidgets
from abc import ABC,abstractmethod

#Balloon is interface a abstract class

N_BALLOONS=15
BALLOON_MISSED='Missed'
BALLOON_MOVING='Balloon Moving'

class Balloon(ABC):
    popSoundLoaded=False
    popSound=None

    @abstractmethod
    def __init__(self,window,maxWidth,maxHeight,ID,objImage,size,nPoints,speedY):
        self.window=window
        self.ID=ID
        self.balloonImage=objImage
        self.size=size
        self.nPoints=nPoints
        self.speedY=speedY
        if not Balloon.popSoundLoaded:
            Balloon.popSoundLoaded=True
            Balloon.popSound=pygame.mixer.Sound('sounds/balloonPop.wav')        

        balloonRect=self.balloonImage.getRect()
        self.width=balloonRect.width
        self.height=balloonRect.height
        self.x=random.randrange(maxWidth-self.width)
        self.y=maxHeight+random.randrange(75)
        self.balloonImage.setLoc((self.x,self.y)) #還沒出現的Small氣球

    def clickedInside(self,mousePoint):
        myRect=pygame.Rect(self.x,self.y,self.width,self.height)
        if myRect.collidepoint(mousePoint):
            Balloon.popSound.play()
            return True,self.nPoints #打中了
        else:
            return False,0
    
    def update(self):
        self.y=self.y-self.speedY  #氣球向上飛的狀況
        self.balloonImage.setLoc((self.x,self.y))
        if self.y <-self.height: #飛出視窗頂端
            return BALLOON_MISSED
        else:
            return BALLOON_MOVING
        
    def draw(self):
        self.balloonImage.draw()

    def __del__(self):
        print(self.size,'Balloon',self.ID, 'is going away') #回收記憶體

    #實作類別
class BalloonSmall(Balloon):
    balloonImage=pygame.image.load('images/redBalloonSmall.png')
    def __init__(self,window,maxWidth,maxHeight,ID):
        objImage=pygwidgets.Image(window,(0,0),BalloonSmall.balloonImage)
        super().__init__(window,maxWidth,maxHeight,ID,objImage,'Small',30,3.1)

class BalloonMedium(Balloon):
    balloonImage=pygame.image.load('images/redBalloonMedium.png')
    def __init__(self,window,maxWidth,maxHeight,ID):
        objImage=pygwidgets.Image(window,(0,0),BalloonMedium.balloonImage)
        super().__init__(window,maxWidth,maxHeight,ID,objImage,'Medium',20,2,2)

class BalloonLarge(Balloon):
    balloonImage=pygame.image.load('images/redBalloonLarge.png')
    def __init__(self,window,maxWidth,maxHeight,ID):
        objImage=pygwidgets.Image(window,(0,0),BalloonLarge.balloonImage)
        super().__init__(window,maxWidth,maxHeight,ID,objImage,'Large',10,1.5)


class BalloonSmall(Balloon):
    balloonImage = pygame.image.load('images/redBalloonSmall.png')
    def __init__(self, window, maxWidth, maxHeight, ID):
        objImage = pygwidgets.Image(window, (0, 0),
                                  BalloonSmall.balloonImage)
        super().__init__(window, maxWidth, maxHeight, ID,
                         objImage, 'Small', 30, 3.1)

class BalloonMedium(Balloon):
    balloonImage = pygame.image.load('images/redBalloonMedium.png')
    def __init__(self, window, maxWidth, maxHeight, ID):
        objImage = pygwidgets.Image(window, (0, 0),
                                  BalloonMedium.balloonImage)
        super().__init__(window, maxWidth, maxHeight, ID,
                         objImage, 'Medium', 20, 2.2)

class BalloonLarge(Balloon):
    balloonImage = pygame.image.load('images/redBalloonLarge.png')
    def __init__(self, window, maxWidth, maxHeight, ID):
        objImage = pygwidgets.Image(window, (0, 0),
                                  BalloonLarge.balloonImage)
        super().__init__(window, maxWidth, maxHeight, ID,
                         objImage, 'Large', 10, 1.5)
