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
        # locationToCenterClick = pyautogui.locateOnScreen('test1.png')
        # print(locationToCenterClick)
        # pyautogui.click(x=350, y=200)
        # pyautogui.click(x=350,y=200, clicks=2, interval=1)
        # pyautogui.getWindow("music").maximize()
        # pyautogui.click(locationToCenterClick, button='left')
        # # print(pyautogui.size())
        # # pyautogui.moveTo(1000, 800)
        # # pyautogui.click()
        # time.sleep(6)
        # pyautogui.typewrite('ls \n', interval=.005)
        
        # pyautogui.click(200, 200);
        # pyautogui.typewrite('Hello world!')
        # pyautogui.typewrite('cd /Users/CommanderCarr/Coding/node/MM/twi-scrape; node indexTwi.js\n', interval=.005)
        # pyautogui.click(pyautogui.locateOnScreen('point1.png'), clicks=1)


        pyautogui.moveTo(100,300)  # move mouse to the window
        pyautogui.dragTo()  # focus the window
        pyautogui.click()  # simulate left click
        pyautogui.typewrite("go run *.go \n")  # type something
        time.sleep(3)

#  pyautogui.typewrite('cd /Users/CommanderCarr/Coding/node/MM/twi-scrape; node indexTwi.js\n', interval=.005)
        
        # pyautogui.click()


    def moveToclick (self, moveToX, moveToY):
        numOfClicks = 1
        pyautogui.click(x=moveToX, y=moveToY, clicks=numOfClicks, button='left')

    # def holdW (self, `hold_time): worl

