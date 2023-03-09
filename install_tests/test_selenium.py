from selenium import webdriver


browser = webdriver.Firefox()
browser.get("http://www.google.com")

with open('selenium.html', 'w') as f:
    f.write(str(browser.page_source))
