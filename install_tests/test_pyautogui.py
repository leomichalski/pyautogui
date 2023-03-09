from pyvirtualdisplay.display import Display
from easyprocess import EasyProcess
import time
import os

disp = Display(visible=True, size=(1366, 768), backend="xvfb", use_xauth=True)
disp.start()
print("DISPLAY STARTED")

proc = EasyProcess(["firefox"])
proc.start()
print("FIREFOX STARTED")

# can't import pyautogui until after display is started
import Xlib.display
import pyautogui
pyautogui._pyautogui_x11._display = Xlib.display.Display(os.environ['DISPLAY'])

# probably enough time to warm up xvfb and firefox
time.sleep(10)
img = pyautogui.screenshot('pyautogui.png')

proc.stop()
disp.stop()
