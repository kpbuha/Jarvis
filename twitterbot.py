from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

def account():
    with open(".vscode\\jarvis\\account.txt",'r') as f:
        info=f.read().split()
        email=info[0]
        pas=info[1]
    return email, pas

email,pas=account()
def tweet(message):
    options=Options()
    options.add_argument("start-maximized")
    driver=webdriver.Chrome(executable_path=".vscode\\jarvis\\chromedriver.exe",options=options)

    driver.get("https://twitter.com/login?lang=en")

    email_xpath="/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input"  
    pas_xpath="/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input"
    login="/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div"

    time.sleep(2)

    driver.find_element_by_xpath(email_xpath).send_keys(email)
    time.sleep(0.5)
    driver.find_element_by_xpath(pas_xpath).send_keys(pas)
    time.sleep(0.5)
    driver.find_element_by_xpath(login).click()
    time.sleep(0.5)
    tweet_xpath='/html/body/div/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div'
    driver.find_element_by_xpath(tweet_xpath).click()
    time.sleep(0.5)
    msg="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div"
    driver.find_element_by_xpath(msg).send_keys(message)
    time.sleep(0.5)
    post="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span"
    driver.find_element_by_xpath(post).click()