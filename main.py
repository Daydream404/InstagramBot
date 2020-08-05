from selenium import webdriver
from time import sleep

username = 'discordpy'
password = 'iMCXcu9zAbjE'

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

def logout():
    sleep(2.1)
    driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/button').click()#settingsbtn
    sleep(2.5)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/div/div[2]/div[2]/div').click()#logout button
    sleep(2.3)
    driver.quit()

main(username,password)
logout()