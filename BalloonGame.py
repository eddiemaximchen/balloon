import pygame
from pygame.locals import *
import pygwidgets
import sys
from BalloonMgr import *

N_BALLOONS=15
BALLOON_MISSED='Missed'
BALLOON_MOVING='Balloon Moving'
BLACK=(0,0,0)
GRAY=(200,200,200)
BACKGROUND_COLOR=(0,180,180)
WINDOW_WIDTH=640
WINDOW_HEIGHT=640
PANEL_HEIGHT=60
USABLE_WINDOW_HEIGHT=WINDOW_HEIGHT-PANEL_HEIGHT
FRAMES_PER_SECOND=30

pygame.init()
window=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock=pygame.time.Clock()

objScoreDisplay=pygwidgets.DisplayText(window,(10,USABLE_WINDOW_HEIGHT+25),'Score: 0',textColor=BLACK,backgroundColor=None,width=140,fontSize=24)

objStatusDisplay=pygwidgets.DisplayText(window,(180,USABLE_WINDOW_HEIGHT+25),'',textColor=BLACK,backgroundColor=None,width=300,fontSize=24)

objStartButton=pygwidgets.TextButton(window,(WINDOW_WIDTH-110,USABLE_WINDOW_HEIGHT+10),'Start')

objBalloonMgr=BalloonMgr(window,WINDOW_WIDTH,USABLE_WINDOW_HEIGHT)
playing=False

while True:
    nPointsEarned=0
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        if playing:
            objBalloonMgr.handleEvent(event) #callback
            theScore=objBalloonMgr.getScore()
            objScoreDisplay.setValue(f'Score: {theScore}')
        elif objStartButton.handleEvent(event):
             objBalloonMgr.start()
             objScoreDisplay.setValue('Score: 0')
             playing=True
             objStartButton.disable()
    if playing:
        objBalloonMgr.update()
        nPopped=objBalloonMgr.getCountPopped()
        nMissed=objBalloonMgr.getCountMissed()
        objStatusDisplay.setValue(f'Popped: {nPopped} Missed: {nMissed} out of: {N_BALLOONS}')

        if (nPopped+nMissed)==N_BALLOONS:
            playing=False
            objStartButton.enable()
    
    window.fill(BACKGROUND_COLOR)

    if playing:
        objBalloonMgr.draw()

    pygame.draw.rect(window,GRAY,pygame.Rect(0,USABLE_WINDOW_HEIGHT,WINDOW_WIDTH,WINDOW_HEIGHT))

    objScoreDisplay.draw()
    objStatusDisplay.draw()
    objStartButton.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)