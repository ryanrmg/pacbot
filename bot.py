import pyscreenshot as ImageGrab
import os
import time
import pynput
import math
#from pynput import mouse, keyboard
from pynput import keyboard
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller
from pynput.keyboard import Key, Listener

"""
http://thesimplearcade.com/play/pacman.html
game url above 
set zoom to 80%  and line up top
"""

#582 * 680


class Bot:


    def __init__(self):
        self.mouse = pynput.mouse.Controller()
        self.board = [0] * 170
        self.keyboard = pynput.keyboard.Controller()
        self.im = ImageGrab.grab(bbox=(429, 176, 1011, 856))
        self.imgrgb = self.im.convert("RGB")
        self.imglist = list(self.imgrgb.getdata())
        self.alive = True


    def startGame(self):
        time.sleep(2)
        self.mouse.scroll(0,2)
        time.sleep(0.3)
        self.mouse.position = (725,655)
        time.sleep(3)
        self.mouse.click(Button.left, 1)
        time.sleep(3)
        #self.startkeyboardlistener()


    def setScreen(self):
        self.im = ImageGrab.grab(bbox=(429, 176, 1011, 856))
        self.imgrgb = self.im.convert("RGB")
        self.imglist = list(self.imgrgb.getdata())


    def getPacPosition(self):
        #pac man position is 251, 255, 0
        try:
            n = self.imglist.index((251, 255, 0))
            return n
        except:
            return 0

    
    def getRedPosition(self):
        #red color is (239,0,0)
        try:
            n = self.imglist.index((239,0,0))
            return n
        except:
            return 0


    def getPinkPosition(self):
        #pink color is (255,145,147)
        try:
            n = self.imglist.index((255,145,147))
            return n
        except:
            return 0


    def getBluePosition(self):
        #blue color is (0,0,255)
        try:
            n = self.imglist.index(0,0,255)
            return n
        except:
            return 0


    def getOrangePosition(self):
        #orange color is (255,151,0)
        try:
            n = self.imglist.index((255,151,0))
            return n
        except:
            return 0


    def pacRight(self):
        self.keyboard.press(Key.right)


    def pacLeft(self):
        self.keyboard.press(Key.left)


    def pacUp(self):
        self.keyboard.press(Key.up)


    def pacDown(self):
        self.keyboard.press(Key.down)


    def imRefresh(self):
        while self.alive:
            time.sleep(0.5)
            self.setScreen()


    def getImageData(self):
        self.im = ImageGrab.grab(bbox=(429, 176, 1011, 856))
        imgrgb = self.im.convert("RGB")
        imglist = list(imgrgb.getdata())
        print(len(imglist))
        return imglist


    def clearBoard(self):
        for i in range(170):
            self.board[i] = 0


    def getBoard(self):
        pos = self.getPacPosition()

        if (pos > 267800) & (pos < 267900):
            self.board[122] = 1



    def getGhostDistance(self, ghost):
        n = self.getPacPosition()
        y1 = round(n / 582)
        x1 = n - (y1 * 582)
        if ghost == 'red':
            k = self.getRedPosition()
        if ghost == 'blue':
            k = self.getBluePosition()
        if ghost == 'orange':
            k = self.getOrangePosition()
        if ghost == 'pink':
            k = self.getPinkPosition()

        y2 = round(k / 582)
        x2 = k - (y2 * 582)


        return math.sqrt( ((x1 - x2) * (x1 - x2)) + ((y1-y2) * (y1-y2)) )


    def randommoves(self):
        t = time.time()
        while time.time() - t < 100000000:
            pos = self.getPacPosition()
            if (time.time() % 1) == 0:
                if pos == self.getPacPosition():
                    self.pacLeft()
                elif pos == self.getPacPosition():
                    self.pacDown()
                elif pos == self.getPacPosition():
                    self.pacRight()




    def setAliveOrDead(self):
        if self.getPacPosition() == 0:
            self.alive = False
        if self.getPacPosition() != 0:
            self.alive = True
#140 * 461







    def on_press(self, key):
        try:
            print('alphanumeric key {0} pressed'.format(
                key.char))
        except AttributeError:
            print('special key {0} pressed'.format(
                key))


    def on_release(self, key):
        print('{0} released'.format(
            key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False


    def startkeyboardlistener(self):
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()