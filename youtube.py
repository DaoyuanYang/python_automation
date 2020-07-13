import time
from selenium import webdriver

'''
# When having private videos returns some error.
# Potentially if playlist too long to load may not exaust the list.
'''

def login(username,password):
    time.sleep(2)
    login_button = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/a/paper-button')\
        .click()
    time.sleep(2)

    # new page, put in email
    email_usnm_input = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')\
        .send_keys(username)    
    next_usnm_but = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div')\
        .click()

    print(driver.current_url)
    # new page, put in password
    time.sleep(2)
    password_input = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')\
        .send_keys(password)
    next_pw_but = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div')\
        .click()
    time.sleep(2)
    try:
        confirm_but = driver.find_element_by_xpath('/html/body/c-wiz[2]/c-wiz/div/div[1]/div/div/div/div[2]/div[3]/div/div[2]/div')\
            .click()
    except:
        pass





def do_after_login(duration):
    '''
    Find playlist and play all the videos with a secs gap
    '''
    searchbox = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')\
        .send_keys('dominic daoyuan')

    searchbotton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
    searchbotton.click()

    # click the channel after searching
    time.sleep(2)
    channel = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-channel-renderer[1]/div/div[2]/a')\
        .click()

    # switch to all the playlists 
    time.sleep(2)
    playlist = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse[2]/div[3]/ytd-c4-tabbed-header-renderer/app-header-layout/div/app-header/div[2]/app-toolbar/div/div/paper-tabs/div/div/paper-tab[3]/div')\
        .click()

    # find playlist 'Tennis Match'
    time.sleep(4)
    all_playls = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse[2]/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]')
    all_playls = all_playls.find_elements_by_css_selector('#video-title') 

    print([x.get_attribute('title') for x in all_playls])
    tns_match_playls = 'Tennis Match playlist'

    for pl in all_playls:
        if pl.get_attribute('title') == 'Tennis Match':
            tns_match_playls = pl
            break

    tns_match_playls.click()   # when clicks on the playlist it automatically plays the first video

    time.sleep(2)
    all_matches = list(driver.find_elements_by_css_selector('#wc-endpoint'))

    # every video plays for 35 secs
    # time.sleep(duration)
    counter = 0
    while True:
        print(f'Playing in loop number {counter}')
        counter += 1
        for video in all_matches[1:]:
            video.click()
            time.sleep(duration)


driver = webdriver.Chrome()
driver.get('http://youtube.com')

username = 'domautotest@gmail.com'
password = 'mypasswordisawesome'
# login(username,password)

do_after_login(35)
driver.close()