# pyvirtualdisplay and easyprocess test
docker run --rm -v ${PWD}:/curr -w /curr leommiranda/pyautogui:libpci-and-libegl python3 test_pyvirtualdisplay.py

# firefox test
docker run --rm -v ${PWD}:/curr -w /curr leommiranda/pyautogui:libpci-and-libegl python3 test_firefox.py

# pyautogui test (no selenium)
docker run --rm -v ${PWD}:/curr -w /curr leommiranda/pyautogui:libpci-and-libegl python3 test_pyautogui.py

# selenium only test (no easyprocess)
docker run --rm -v ${PWD}:/curr -w /curr leommiranda/pyautogui:libpci-and-libegl bash -c "
    Xvfb :1 -screen 0 1024x768x16 &> xvfb.log  & \
    export DISPLAY=:1.0; \
    python3 test_selenium.py;
"

# pyautogui and selenium test (no easyprocess)
docker run --rm -v ${PWD}:/curr -w /curr leommiranda/pyautogui:libpci-and-libegl python3 test_selenium_and_pyautogui.py
