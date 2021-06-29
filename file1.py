from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import json
import requests
from getpass import getpass
from textblob import TextBlob
import re

driver = webdriver.Chrome('C:/Users/...../chromedriver.exe')
driver.get('https://twitter.com/')

choose_login = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]"))).click()

username = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='session[username_or_email]']")))
password = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='session[password]']")))

username.clear()
password.clear()

enter_user = input("enter phone, username or email")
enter_pass = getpass()

username.send_keys(enter_user)
password.send_keys(enter_pass)

login_btn = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div")))
login_btn.click()

target_username = input("enter username")

driver.execute_script(f'''window.open("{target_username}", "_blank");''')
driver.switch_to.window(driver.window_handles[-1])

followers = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div[2]/a")))
followers.click()


def clean_text(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text) # remove @mentions
    text = re.sub(r'#', '', text) # remove #symbols
    text = re.sub(r'RT[\s]+', '', text) # remove RT
    text = re.sub(r'https?:\/\/S+', '', text) # remove https
    return text
    
list_followers = driver.find_elements_by_xpath("//div[@data-testid='UserCell']")

scroll_height = 100
for i in range(len(list_followers[0:10])):
    list_followers[i].click()
    time.sleep(3)
    tweets = driver.find_elements_by_xpath("//div[@data-testid='tweet']")
    negative_counter = 0
    positive_counter = 0
    for i in range(len(tweets[:2])):
        tb = TextBlob(clean_text(tweets[i].text))
        pol = tb.sentiment.polarity
        if(pol < 0.3):
            negative_counter += 1
        else:
            positive_counter += 1
    if(negative_counter > positive_counter):
        dots3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div/div[1]")))
        dots3.click()
        time.sleep(1)
        block = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='block']")))
        block.click()
        time.sleep(1)
        block_yes = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div[3]/div[2]")))
        block_yes.click()
        time.sleep(1)
        back = driver.find_elements_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[1]")
        back[0].click()
        time.sleep(3)
        driver.execute_script(f'''window.scrollTo(0, {scroll_height});''')
        time.sleep(1)
        list_followers = driver.find_elements_by_xpath("//div[@data-testid='UserCell']")
        time.sleep(1)
        scroll_height += 100
    else:
        back = driver.find_elements_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[1]")
        back[0].click()
        time.sleep(3)
        driver.execute_script(f'''window.scrollTo(0, {scroll_height});''')
        time.sleep(1)
        list_followers = driver.find_elements_by_xpath("//div[@data-testid='UserCell']")
        time.sleep(1)
        scroll_height += 100
