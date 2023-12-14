
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import UserstoFollow
import message_to_stalked
from UserInfo import email, password


class InstaBot:
    def __init__(self, email, password):
        self.browse = webdriver.Chrome()
        self.email = email
        self.password = password

    def login(self):
        self.browse.get("https://www.instagram.com/")
        time.sleep(2)
     
        emailInput = self.browse.find_element(By.NAME, "username")
        passwordInput = self.browse.find_element(By.NAME, "password")
    
        emailInput.send_keys(self.email)
        time.sleep(2)
        passwordInput.send_keys(self.password)
        time.sleep(2)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(10)

    def get_followings(self):
        get_victim = "dann_k07"
        
        self.browse.get(f"https://www.instagram.com/{get_victim}")
        time.sleep(5)
        
        open_dialog = self.browse.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/ul/li[3]/a")
        time.sleep(3)        
        open_dialog.click()
        
        dialogMenu = open_dialog.find_element(By.CSS_SELECTOR, "div[role=dialog] ul")
        followingCount = len(dialogMenu.find_element(By.CSS_SELECTOR,"li"))
            
        action = webdriver.ActionChains(self.browse)
        time.sleep(5)

        while True:
            dialogMenu.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            
            time.sleep(2)

            newCount = len(dialogMenu.find_element(By.CSS_SELECTOR, "li"))

            if followingCount != newCount:
                followingCount = newCount
                print(f"UpdatedCount : {followingCount}")
                time.sleep(2)
            else:
                break

    
        followings = dialogMenu.find_elements(By.CSS_SELECTOR, "li")
        followingsList = []

        for user in followings:
            user_link = user.find_elements(By.CSS_SELECTOR, "a").get_attribute("href")
            followingsList.append(user_link)

        save_followings = 'C:/Users/abdul/Desktop/Selenium/followings'

        with open(save_followings, "w") as file:
            for element in followingsList:
                file.write(f"{element}\n")

    def follow_page(self):
        to_follow = UserstoFollow.Follow_list

        for user_link in to_follow:
            self.browse.get(f"https://www.instagram.com/{user_link}")
            time.sleep(5)
            
            follow_button = self.browse.find_element(By.XPATH, '//button[@class=" _acan _acap _acas _aj1- _ap30"]')
            time.sleep(5)
            follow_button.click()
            
            time.sleep(10)

    def message_func(self):
        to_message = UserstoFollow.Follow_list

        my_message = message_to_stalked.my_message_st

        self.browse.get(f"https://www.instagram.com/{to_message}")
        time.sleep(5)

        message_button_path = '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/div/div[2]/div'
        message_button = self.browse.find_element(By.XPATH, message_button_path)

        time.sleep(5)
        message_button.click()
        time.sleep(5)
            
        message_box_xpath = self.browse.find_element(By.XPATH, '//div[@role="textbox"]')
        time.sleep(5)
        
        message_box_xpath.click()
        time.sleep(5)
       
        message_box_xpath.send_keys(my_message)
        time.sleep(5)
            
        message_box_xpath.send_keys(Keys.ENTER)
        time.sleep(8)

        
# Base
Bot = InstaBot(email, password)


# Run by Choice

start = input("""Modes : 

1 -- Follow a List of Users     2 -- Message a List of Users
                  
3 -- Get Followings List        4 -- Exit

Choice : """)
time.sleep(2)

try:
    if start == "1":
        time.sleep(0.5)
        print("\nBot Started")
        Bot.login()
        time.sleep(5)
        Bot.follow_page()
        
    elif start == "2":
        time.sleep(0.5)
        print("\nBot Started")
        Bot.login()
        time.sleep(5)
        Bot.message_func() 
        # Message function is for visible accounts or the accounts you follow

    elif start == "3":
        time.sleep(0.5)
        print("\nBot Started")
        Bot.login()
        time.sleep(5)
        Bot.get_followings()

    elif start == "4":
        time.sleep(1)
        print("\nAlright!!!")
        sys.exit(0)

    else:
        time.sleep(1)
        print("\nInvalid Input!")
        sys.exit(0)
        
except KeyboardInterrupt:
    print("Alright!!!")
    sys.exit(0)
