import pyscreenshot as ImageGrab
import time
import pynput
#from pynput import mouse, keyboard
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller




mouse = pynput.mouse.Controller() 
mouse.position  = (500,350)
mouse.click(Button.left, 1)


for k in range(100000000):
    im = ImageGrab.grab(bbox=(400, 200, 500, 300))
    imrgb = im.convert("RGB")
    imglist = list(imrgb.getdata())
    for i in range(5):
        if imglist[i] == (0, 229, 96):
            mouse.click(Button.left, 1)