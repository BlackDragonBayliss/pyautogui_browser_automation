import time, pyautogui

class AutomationManager:
    def __init__(self):
        cortexicalThought = []
 
    def exitBrowser(self):
        # print("exiting"
        print(pyautogui.position())
        locationToCenterClick = pyautogui.locateOnScreen('browserQuitCenterLocation1.png')
        # print(pyautogui.locateOnScreen('browserQuitCenterLocation1.png'))
        pyautogui.doubleClick(x=moveToX, y=moveToY)


    def findCenter(self):
        # print(center())
        pass
 
    def operationStartCMDClickCenter(self):
        print("inside")
        # locationToCenterClick = pyautogui.locateOnScreen('targetClick.png')
        # pyautogui.click(x=350, y=1300)
        # print(pyautogui.size())
        # pyautogui.moveTo(1000, 800)
        pyautogui.click()
        time.sleep(6)
        pyautogui.typewrite('Hello world!\n', interval=2)
        # pyautogui.click()


    def moveToclick (self, moveToX, moveToY):
        numOfClicks = 1
        pyautogui.click(x=moveToX, y=moveToY, clicks=numOfClicks, button='left')

    def holdW (self, hold_time):
        start = time.time()
        while time.time() - start < hold_time:
            pyautogui.press('w')
