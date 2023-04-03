import pygame
from pygame.locals import *
import random
import pygwidgets
from Balloon import *

N_BALLOONS=15
BALLOON_MISSED='Missed'
BALLOON_MOVING='Balloon Moving'

class BalloonMgr():
    def __init__(self,window,maxWidth,maxHeight):
        self.window=window
        self.maxWidth=maxWidth
        self.maxHeight=maxHeight
    
    def start(self):
        self.balloonList=[]
        self.nPopped=0
        self.nMissed=0
        self.score=0

        for balloonNum in range(0,N_BALLOONS):
            randomBalloonClass=random.choice((BalloonSmall,BalloonMedium,BalloonLarge))
            objBalloon=randomBalloonClass(self.window,self.maxWidth,self.maxHeight,balloonNum)
            self.balloonList.append(objBalloon)


    def handleEvent(self,event):
        if event.type ==MOUSEBUTTONDOWN:
            #最頂端的氣球會消失
            for objBalloon in reversed(self.balloonList):
                wasHit, nPoints=objBalloon.clickedInside(event.pos)
                if wasHit:
                    if nPoints>0:
                        self.balloonList.remove(objBalloon) #打中了所以移除
                        self.nPopped=self.nPopped+1
                        self.score=self.score+nPoints
                    return
                
    def update(self):
        for objBalloon in self.balloonList:
            status=objBalloon.update()
            if status==BALLOON_MISSED:
               self.balloonList.remove(objBalloon) #到頂了所以移除
               self.nMissed=self.nMissed+1

    def getScore(self):
        return self.score

    def getCountPopped(self):
        return self.nPopped

    def getCountMissed(self):
        return self.nMissed

    def draw(self):
        for objBallooon in self.balloonList:
            objBallooon.draw() 