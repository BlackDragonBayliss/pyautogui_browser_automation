import pyautogui
from automationManager import AutomationManager
def main():
    print("hit")
    pyautogui.moveTo(900,300)  # move mouse to the window
    pyautogui.dragTo()  # focus the window
    pyautogui.click()  # simulate left click
    # pyautogui.typewrite("go run *.go \n")  # type something
    pyautogui.press('up')
    pyautogui.press('enter')
    # automationManager = AutomationManager()
    #             # automationManager.exitBrowser()
    # automationManager.operationStartCMDClickCenter()

if __name__ == "__main__": main()