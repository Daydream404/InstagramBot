from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import random
import instaloader

username = open("D:\\Python\\DiscordPyIG\\ig_name.txt", "r").read()
password = open("D:\\Python\\DiscordPyIG\\ig_pass.txt", "r").read()
#hashtag = '#pythonprogramming'
hashtag = '#programmercommunity'
number = 0

driver = webdriver.Chrome('D:/Python/DiscordPyIG/chromedriver')

def rndnum():
    number = random.uniform(5.1,15.8)
    print("Sleeping for",number, "sec")
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


def following():
    instg = instaloader.Instaloader()
    PROFILE = "discordpy"
    username = "discordpy"
    instg.login(username, password)
    profile = instaloader.Profile.from_username(instg.context, PROFILE)

    open('following.txt', 'w').close()

    file = open("following.txt","a+")
    for flwing in profile.get_followees():
        username = flwing.username
        file.write(username + "\n")

    file.close()

    with open ('following.txt', 'rt') as myfile:
        ig_profiles = myfile.read()
    


def likes():
    instg = instaloader.Instaloader()
    PROFILE = "discordpy"
    username = "discordpy"
    instg.login(username, password)
    profile = instaloader.Profile.from_username(instg.context, PROFILE)

    open('following.txt', 'w').close()

    file = open("following.txt","a+")
    for flwing in profile.get_followees():
        username = flwing.username
        file.write(username + "\n")

    file.close()

    with open ('following.txt', 'rt') as myfile:
        ig_profiles = myfile.read()

    driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys(hashtag)
    rndnum()
    driver.find_element_by_class_name("z556c").click()
    rndnum()
    driver.find_element_by_class_name("eLAPa").click()
    rndnum()
    for i in range(35):
        instg = instaloader.Instaloader()
        PROFILE = "discordpy"
        username = "discordpy"
        instg.login(username, password)
        profile = instaloader.Profile.from_username(instg.context, PROFILE)

        open('following.txt', 'w').close()

        file = open("following.txt","a+")
        for flwing in profile.get_followees():
            username = flwing.username
            file.write(username + "\n")

        file.close()

        with open ('following.txt', 'rt') as myfile:
            ig_profiles = myfile.read()

        acc_name = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div/header/div[2]/div[1]/div[1]/span/a").get_attribute("innerHTML").splitlines()[0]
        like = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div/div[3]/section[1]/span[1]/button').click()#like button
        rndnum()
        if acc_name in ig_profiles:
            pass
        else:
            follow = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div/header/div[2]/div[1]/div[2]/button').click()
            rndnum()
        
        # cancel = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
        driver.find_element_by_class_name("coreSpriteRightPaginationArrow").click()
        rndnum()
        
    driver.find_element_by_xpath("/html/body/div[4]/div[3]/button").click()
    rndnum()
    driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(username)).click()


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