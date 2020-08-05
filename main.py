from selenium import webdriver
from time import sleep

username = open("D:\\Python\\DiscordPyIG\\ig_name.txt", "r").read()
password = open("D:\\Python\\DiscordPyIG\\ig_pass.txt", "r").read()
hashtag = '#pythonprogramming'

driver = webdriver.Chrome('D:/Python/DiscordPyIG/chromedriver')

def main(username, password):
    driver.get('https://instagram.com')
    sleep(2)
    driver.find_element_by_xpath('//input[@name=\"username\"]').send_keys(username)
    sleep(4)
    driver.find_element_by_xpath('//input[@name=\"password\"]').send_keys(password)
    sleep(5)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    sleep(6)
    driver.find_element_by_xpath('//button[contains(text(), "Not Now")]').click()
    sleep(3)
    driver.find_element_by_xpath('//button[contains(text(), "Not Now")]').click()
    sleep(4)

def likes():
    driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys(hashtag)
    sleep(2)
    driver.find_element_by_class_name("z556c").click()
    sleep(2)
    driver.find_element_by_class_name("eLAPa").click()
    sleep(2.5)
    driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div/div[3]/section[1]/span[1]/button').click()#like button
    sleep(3)
    driver.find_element_by_class_name("coreSpriteRightPaginationArrow").click()
    sleep(2.3)
    


def logout():
    sleep(2.1)
    driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/button').click()#settingsbtn
    sleep(2.5)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/div/div[2]/div[2]/div').click()#logout button
    sleep(2.3)
    driver.quit()


main(username,password)
likes()
#logout()