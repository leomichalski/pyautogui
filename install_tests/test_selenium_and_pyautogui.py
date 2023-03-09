import os
import time
from selenium import webdriver
from pyvirtualdisplay.display import Display
from easyprocess import EasyProcess

disp = Display(visible=True, size=(1366, 768), backend="xvfb", use_xauth=True)
disp.start()
print("DISPLAY STARTED")

# can't import pyautogui until after display is started
import Xlib.display
import pyautogui
pyautogui._pyautogui_x11._display = Xlib.display.Display(os.environ['DISPLAY'])

# imports and display start are done, so we can start to use selenium and pyautogui
browser = webdriver.Firefox()

browser.get("http://www.google.com")

with open('pyautogui_and_selenium.html', 'w') as f:
    f.write(str(browser.page_source))

img = pyautogui.screenshot('pyautogui_and_selenium.png')

disp.stop()
