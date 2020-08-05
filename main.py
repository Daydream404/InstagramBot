from selenium import webdriver
from time import sleep
import random

username = open("D:\\Python\\DiscordPyIG\\ig_name.txt", "r").read()
password = open("D:\\Python\\DiscordPyIG\\ig_pass.txt", "r").read()
hashtag = '#pythonprogramming'
number = 0

driver = webdriver.Chrome('D:/Python/DiscordPyIG/chromedriver')

def rndnum():
    number = random.uniform(2.1,8.1)
    sleep(number)


def main(username, password):
    driver.get('https://instagram.com')
    rndnum()
    driver.find_element_by_xpath('//input[@name=\"username\"]').send_keys(username)
    rndnum()
    driver.find_element_by_xpath('//input[@name=\"password\"]').send_keys(password)
    rndnum()
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    rndnum()
    driver.find_element_by_xpath('//button[contains(text(), "Not Now")]').click()
    rndnum()
    driver.find_element_by_xpath('//button[contains(text(), "Not Now")]').click()
    rndnum()


def likes():
    driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys(hashtag)
    rndnum()
    driver.find_element_by_class_name("z556c").click()
    rndnum()
    driver.find_element_by_class_name("eLAPa").click()
    rndnum()
    for i in range(10):
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div/div[3]/section[1]/span[1]/button').click()#like button
        rndnum()
        driver.find_element_by_class_name("coreSpriteRightPaginationArrow").click()
        rndnum()
        

def logout():
    rndnum()
    driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/button').click()#settingsbtn
    rndnum()
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/div/div[2]/div[2]/div').click()#logout button
    rndnum()
    driver.quit()


main(username,password)
likes()
#logout()