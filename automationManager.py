import time, pyautogui

class AutomationManager:
    def __init__(self):
        cortexicalThought = []
 
    def exitBrowser(self):
        # print("exiting"
        print(pyautogui.position())
        locationToCenterClick = pyautogui.locateOnScreen('point1.png')
        # print(pyautogui.locateOnScreen('browserQuitCenterLocation1.png'))
        pyautogui.doubleClick(x=moveToX, y=moveToY)


    def findCenter(self):
        # print(center())
        pass
 
    def operationStartCMDClickCenter(self):
        print("operationStartCMDClickCenter")

        pyautogui.moveTo(900,300)  # move mouse to the window
        pyautogui.dragTo()  # focus the window
        pyautogui.click()  # simulate left click
        # pyautogui.typewrite("go run *.go \n")  # type something
        pyautogui.press('up')
        pyautogui.press('enter')
        
        pyautogui.moveTo(100,300)  # move mouse to the window
        pyautogui.dragTo()  # focus the window
        pyautogui.click()  # simulate left click
        # pyautogui.typewrite("go run *.go \n")  # type something
        pyautogui.press('up')
        pyautogui.press('enter')
        time.sleep(1)

        

    def moveToclick (self, moveToX, moveToY):
        numOfClicks = 1
        pyautogui.click(x=moveToX, y=moveToY, clicks=numOfClicks, button='left')

    # def holdW (self, `hold_time): worl

