## Install tests

### TL;DR

#### Run the following command:

```
sh run_tests.sh
```

Check if the files 'pyvirtualdisplay.png', 'firefox.png', 'pyautogui.png', and 'selenium_and_pyautogui.png' are in the current folder. Also check if they are like the files in the 'outputs' folder.

Check if the files 'selenium.html' and 'selenium_and_pyautogui.html' both contain '[google.com](https://www.google.com/)' html code. 

### Long version

#### Before each test, stop and run the container with the following command:

```
docker run --rm -it -v ${PWD}:/curr -w /curr leommiranda/pyautogui bash
```

#### 1. Test if pyvirtualdisplay works
Warning: stop and rerun the container between each test.

```
python3 test_pyvirtualdisplay.py
```

Wait a bit. Then check if the 'pyvirtualdisplay.png' image is like the following image:

![pyvirtualdisplay test image](/install_tests/outputs/standard_pyvirtualdisplay.png)


#### 2. Test if firefox works (depends on pyvirtualdisplay test)
Warning: stop and rerun the container between each test.

```
python3 test_firefox.py
```

Wait a bit. Then check if the 'firefox.png' image is like the following image:

![firefox test image](/install_tests/outputs/standard_firefox.png)

#### 3. Test if pyautogui works (depends on firefox test)
Warning: stop and rerun the container between each test.

```
python3 test_pyautogui.py
```

Wait a bit. Then check if firefox is in the 'pyautogui.png' screenshot. Like the following image:

![pyautogui test image](/install_tests/outputs/standard_pyautogui.png)


#### 4. Test if xvfb and selenium work. 

```
Xvfb :1 -screen 0 1024x768x16 &> xvfb.log  &
export DISPLAY=:1.0
python3 test_selenium.py
```

Wait a minute. If the file 'selenium.html' contains the [google.com](http://www.google.com) html, then the test worked.

#### 5. Test if pyautogui and selenium work.

```
python3 test_selenium_and_pyautogui.py
```

Wait a minute.

If the file 'selenium_and_pyautogui.html' contains the [google.com](http://www.google.com) html, then selenium worked.

If firefox is in the 'selenium_and_pyautogui.png' screenshot, then pyautogui worked. Like the following image:

![selenium and pyautogui test image](/install_tests/outputs/standard_pyautogui_and_selenium.png)
