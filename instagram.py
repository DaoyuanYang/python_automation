import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://instagram.com')


def sleep():
    time.sleep(5)


### click 'Log in with Facebook' 
sleep()
login_fb = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[6]/button").click()


### login with facebook
sleep()
fb_usnm = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[1]/input')\
    .send_keys('yangdaoyuan172526@gmail.com')
fb_password = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[2]/input')\
    .send_keys('Domey1999$')
sleep()
login_button = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[3]/button')\
    .click()


### we are in instagram now 
# and click 'not now' for qustion alert 'turn on notification now?'
sleep()
try:
    dont_turn_on_notificaion = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')\
        .click()
except:
    pass


### scroll to the bottom of the page (infinitely)
SCROLL_PAUSE_TIME = 5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


