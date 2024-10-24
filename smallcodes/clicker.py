import pyautogui
import keyboard
import time as t

pwd = pyautogui.password(text="Enter Password", title="Password", default="", mask="*")
if pwd == "yes":

    while keyboard.is_pressed("q") == False:
        pyautogui.click()
        t.sleep(0.1)
