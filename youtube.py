from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://youtube.com')

searchbox = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
searchbox.send_keys('dominic daoyuan')

searchbotton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchbotton.click()

channelXpath = '/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer'
contentSection = driver.find_element_by_xpath(channelXpath)
targetchannel = driver.find_element_by_xpath('.')


targetchannel.click()