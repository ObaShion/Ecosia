#推奨環境：Jupyter lab
from selenium import webdriver
import time
browser = webdriver.Chrome(ChromeDriverManager().install())
from webdriver_manager.chrome import ChromeDriverManager

browser.get("https://www.ecosia.org")
elem_username = browser.find_element_by_xpath('//*[@id="__layout"]/div/div/header/div/div[2]/form/div[1]/input')
elem_username.send_keys('Ecosia')
elem_enter = browser.find_element_by_xpath('//*[@id="__layout"]/div/div/header/div/div[2]/form/div[2]/button[2]')
elem_enter.click()

#これを一回実行する
time.sleep(1)
elem_tag = browser.find_element_by_xpath('/html/body/div[1]/div/nav[1]/div[1]/div/div[2]/div/form/div[2]/div[3]/a')
time.sleep(2)
elem_tag.click()
time.sleep(1)
elem_username = browser.find_element_by_xpath('//*[@id="__layout"]/div/div/header/div/div[2]/form/div[1]/input')
elem_username.send_keys('Ecosia')
elem_enter = browser.find_element_by_xpath('//*[@id="__layout"]/div/div/header/div/div[2]/form/div[2]/button[2]')
elem_enter.click()

#2回目以降はこっちをループさせる
try:
    while True:
        elem_tag = browser.find_element_by_xpath('/html/body/div/div/div/div[1]/header/div[1]/div[1]/a')
        elem_tag.click()
        time.sleep(1)
        elem_username = browser.find_element_by_xpath('//*[@id="__layout"]/div/div/header/div/div[2]/form/div[1]/input')
        elem_username.send_keys('Ecosia')
        elem_enter = browser.find_element_by_xpath('//*[@id="__layout"]/div/div/header/div/div[2]/form/div[2]/button[2]')
        elem_enter.click()
except KeyboardInterrupt:
    print('!!FINISH!!')

