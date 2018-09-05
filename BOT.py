from pygame import *
import pyautogui
import time
o = open('parse','r')

def moveRight():
    pyautogui.keyDown('right')
    time.sleep(.5)
    pyautogui.keyUp('right')

def moveUp():
    pyautogui.keyDown('up')
    time.sleep(.5)
    pyautogui.keyUp('up')

def moveDown():
    pyautogui.keyDown('down')
    time.sleep(.5)
    pyautogui.keyUp('down')

def moveLeft():
    pyautogui.keyDown('left')
    time.sleep(.5)
    pyautogui.keyUp('left')

def itemLeft():
    pyautogui.click(700, 700, duration=.25)

def itemRight():
    pyautogui.moveTo(770, 700, duration=.25)
    return pyautogui.click(770, 700, duration=.25)

def useItemButton():
    pyautogui.moveTo(750, 730, duration=.25)
    return pyautogui.click(750, 730, duration=.25)

def fightButton():
    pyautogui.moveTo(750, 680, duration=.25)
    return pyautogui.click(750, 680, duration=.25)

def pokemonButton():
    pyautogui.moveTo(750, 720, duration=.25)
    return  pyautogui.click(750, 720, duration=.25)

def runButton():
    pyautogui.moveTo(870, 720, duration=.25)
    return pyautogui.click(870, 720, duration=.25)

def bagButton():
    pyautogui.moveTo(870, 680, duration=.25)
    return pyautogui.click(870, 680, duration=.25)
def moveOFF():
    pyautogui.moveTo(500, 500, duration=.25)



def grassKill():
    moveOFF()
    time.sleep(3)
    fightButton()
    time.sleep(.5)
    moveOFF()
    fightButton()

def kill():
    moveOFF()
    time.sleep(3)
    fightButton()
    time.sleep(.5)
    moveOFF()
    fightButton()


def catchem():
    moveOFF()
    time.sleep(3)
    fightButton()
    time.sleep(.5)
    moveOFF()
    fightButton()
    time.sleep(1)
    bagButton()
    time.sleep(.5)
    itemRight()
    time.sleep(.5)
    moveOFF()
    itemRight()
    time.sleep(.5)
    useItemButton()

def runFromFight():
    moveOFF()
    time.sleep(3)
    runButton()
    moveOFF()
    runButton()



def pathOne():
    pyautogui.press('left')
    pyautogui.press('up')
    pyautogui.press('right')
    pyautogui.press('right')
    pyautogui.press('down')
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('up')
    pyautogui.press('right')
    pyautogui.press('right')
    pyautogui.press('down')
    pyautogui.press('left')


def pathTwo():
    pyautogui.press('right')
    pyautogui.press('left')
    pyautogui.press('right')
    pyautogui.press('left')
    pyautogui.press('right')
    pyautogui.press('left')
    pyautogui.press('right')
    pyautogui.press('left')
    pyautogui.press('right')
    pyautogui.press('left')

def pathThree():
    pyautogui.press('up')
    pyautogui.press('down')
    pyautogui.press('up')
    pyautogui.press('down')
    pyautogui.press('up')
    pyautogui.press('down')
    pyautogui.press('up')
    pyautogui.press('down')
    pyautogui.press('up')
    pyautogui.press('down')
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.press('down')
    pyautogui.press('up')
    pyautogui.press('down')
    pyautogui.press('up')

def optimalPath1(x):
    moveUp()
    moveDown()
    moveUp()

#getGameRegion()
#while True:
  #  file = open('parse','r')
 #   optimalPath1(stepCount)
    #for i in o:
        #name of who you want
     #   if '' in i:
            #what you want the bot to do to catch or fight the opponent.


    #print(len('b\xe4\xa4q\xebJ\xb0\x00\x00\xca\x11"3\x08\x00E \x00\x95\x1d\x06@\x004\x06\x03.\x9eE}\xbf\n\x00\x00\x0b${\n$\xd2\xa9\xfd\xe7\x1a-h\x12P\x18\x018\x00\x19\x00\x00'))