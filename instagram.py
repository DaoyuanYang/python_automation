import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def login_with_fb():    
    ### click 'Log in with Facebook' 
    time.sleep(5)
    login_fb = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[6]/button").click()


    ### login with facebook
    time.sleep(3)
    fb_usnm = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[1]/input')\
        .send_keys('yangdaoyuan172526@gmail.com')
    fb_password = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[2]/input')\
        .send_keys('Domey1999$')
    login_button = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[3]/button')\
        .click()

    print('Logged in with Facebook')


def setup_inst():
    ### we are in instagram now 
    # and click 'not now' for qustion alert 'turn on notification now?'
    time.sleep(5)
    try:
        dont_turn_on_notificaion = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')\
            .click()
    except:
        pass


def scroll_to_bottom():
    ### scroll to the bottom of the page (infinitely)
    SCROLL_PAUSE_TIME = 10

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
    print('Scrolled to Bottom or Scrolling timed out')


def like_posts():
    ### search channel
    time.sleep(3)
    searchbar = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div/div')\
        .click()
    searchbar_input = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
    searchbar_input.send_keys('tennis_simplified')
    
    count = 0
    for i in range(5):
        time.sleep(3)
        print(f'Pressing ENTER {count}')
        try:
            searchbar_input.send_keys(Keys.ENTER)
        except:
            print('Stopped pressing ENTER')
            break
        count += 1

    print('Hit enter')

    ### scroll to the bottom
    scroll_to_bottom()

    ### like posts
    post_section = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[2]/article/div/div')
    all_posts = post_section.find_elements_by_css_selector('#react-root > section > main > div > div._2z6nI > article > div > div > div > div > a')
    all_posts = [x.get_attribute('href') for x in all_posts]

    post_count = 0
    for link in all_posts:
        print(f'Working on post number {post_count}')
        driver.get(link)
        time.sleep(5)

        like_but = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button')
        like_status = like_but.find_element_by_css_selector('svg').get_attribute('aria-label')
        if like_status == 'Like':
            like_but.click()
            print(f'Post number {post_count} was not liked, performed like')
        time.sleep(5)
        post_count += 1


driver = webdriver.Chrome()
driver.get('http://instagram.com')

login_with_fb()
setup_inst()
like_posts()
driver.quit()
