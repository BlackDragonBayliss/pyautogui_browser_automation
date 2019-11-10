import pyautogui

class AutomationManager:
    def __init__(self):
        cortexicalThought = []
 
    def exitBrowser(self):
        # print("exiting"
        # print(pyautogui.position())
        locationToCenterClick = pyautogui.locateOnScreen('browserQuitCenterLocation1.png')
        # print(pyautogui.locateOnScreen('browserQuitCenterLocation1.png'))
        pyautogui.doubleClick(x=moveToX, y=moveToY)