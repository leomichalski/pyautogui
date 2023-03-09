from easyprocess import EasyProcess
from pyvirtualdisplay.smartdisplay import SmartDisplay


with SmartDisplay() as disp:
    with EasyProcess(["firefox"]):
        img = disp.waitgrab()

img.save("firefox.png")
