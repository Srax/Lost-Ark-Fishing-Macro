from pynput.keyboard import Key, Controller, Listener
import pyautogui
import keyboard as kb
import random
import pygetwindow as gw
import time
import decimal

lostArkWindow = gw.getWindowsWithTitle("Lost Ark")[0]
keyboard = Controller()
isRunning = True
cycleCount = 0
quitKey = 'q'

def isFishing():
    # if quitButtonIsPressed(False):
    return pyautogui.locateOnScreen("img/fishing-active.png", confidence = 0.7) != None
def isBite():
    # if quitButtonIsPressed(False):
    return pyautogui.locateOnScreen("img/exclamation2.png", confidence = 0.75) != None
def isFishingMenuOpen():
    # if quitButtonIsPressed(False):
    return pyautogui.locateOnScreen("img/fishMenuOpen.png", confidence = 0.8) != None
def isRegularPointer():
    # if quitButtonIsPressed(False):
    return pyautogui.locateOnScreen("img/regularpointer2.png", confidence = 0.65) != None



def quitButtonIsPressed(bool):
    if kb.is_pressed(quitKey) == bool:
        return setIsRunning(False)
    return False
def setIsRunning(val):
    global isRunning
    isRunning = val
    exit("Exitting...")

def generateRandomDecimalValue(min, max):
   return round(random.uniform(min, max), 2)
   
def runFishingCycle():
    if isFishing():
            print("We are fishing!")
            time.sleep(generateRandomDecimalValue(0.1,0.5))
            if isBite():
                print("Attempting to catch fish!")
                time.sleep(generateRandomDecimalValue(0.1,0.25))
                pyautogui.press('e')
    else:
        print("Not fishing")
        pyautogui.press('e')
        time.sleep(generateRandomDecimalValue(3,5))



while isRunning == True:
    if quitButtonIsPressed(True):
        break
    else:
        if gw.getActiveWindow() == lostArkWindow:
            if isFishingMenuOpen():
                runFishingCycle()
            else:
                print("Please open the fish menu (B)")
                time.sleep(2)
        else:
            print("Lost Ark is not running in the foreground!")
            print("To continue, tab into the game and keep the window open!\n")
            time.sleep(5)
    