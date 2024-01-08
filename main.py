import sys
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import Victims
import BotAccounts
import yourMessage
from YourIG import username, password


class InstaBot:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')

        self.browse = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.browse.get("https://www.instagram.com/login")
        sleep(2)
     
        nameInput = self.browse.find_element(By.NAME, "username")
        passwordInput = self.browse.find_element(By.NAME, "password")
    
        nameInput.send_keys(username)
        sleep(2)
        passwordInput.send_keys(password)
        sleep(2)
        passwordInput.send_keys(Keys.ENTER)
        sleep(10)

    def get_followings(self):

        for get_victim in Victims.victim_list:
        
            self.browse.get(f"https://www.instagram.com/{get_victim}")
            sleep(5)

            open_dialog = self.browse.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/ul/li[3]/a")
            sleep(3)
            open_dialog.click()

            dialogMenu = open_dialog.find_element(By.CSS_SELECTOR, "div[role=dialog] ul")
            followingCount = len(dialogMenu.find_element(By.CSS_SELECTOR,"li"))

            action = webdriver.ActionChains(self.browse)
            sleep(5)

            while True:
                dialogMenu.click()
                action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()

                sleep(2)

                newCount = len(dialogMenu.find_element(By.CSS_SELECTOR, "li"))

                if followingCount != newCount:
                    followingCount = newCount
                    print(f"UpdatedCount : {followingCount}")
                    sleep(2)
                else:
                    break

            followings = dialogMenu.find_elements(By.CSS_SELECTOR, "li")
            followingsList = []

            for user in followings:
                user_link = user.find_elements(By.CSS_SELECTOR, "a").get_attribute("href")
                followingsList.append(user_link)

            save_followings = '.../followings'

            with open(save_followings, "a") as file:
                for element in followingsList:
                    file.write(f"{element}\n")

    def follow_page(self):
        to_follow = Victims.victim_list

        for user_link in to_follow:
            self.browse.get(f"https://www.instagram.com/{user_link}")
            sleep(5)
            
            follow_button = self.browse.find_element(By.XPATH, '//button[@class=" _acan _acap _acas _aj1- _ap30"]')
            sleep(5)
            follow_button.click()
            
            sleep(10)

    def message_func(self):
        my_message = yourMessage.msg_str
        victims = Victims.victim_list

        count = 0

        try:
            for victim in victims:
                self.browse.get('https://www.instagram.com/direct/new/')
                sleep(5)

                to_btn = self.browse.find_element(By.NAME, 'queryBox')
                to_btn.send_keys(victim)

                sleep(8)

                chk_mrk = self.browse.find_element(By.CLASS_NAME, 'dCJp8')
                chk_mrk.click()

                sleep(3)

                nxt_btn = self.browse.find_element(By.XPATH, '//div[@class="mXkkY KDuQp"]')
                nxt_btn.click()

                sleep(6)

                txt_box = self.browse.find_element(By.TAG_NAME, 'textarea')
                txt_box.send_keys(f"{my_message}")

                sleep(2)

                snd_btn = self.browse.find_element(By.CSS_SELECTOR, '.sqdOP.yWX7d.y3zKF')
                snd_btnn = snd_btn[len(snd_btn)-1]
                snd_btnn.click()

                sleep(4)
                count += 1

            print(f"\nSent : {count} \n")

        except TypeError:
            print('Failed!')

    def view_story(self):
        main_acc = BotAccounts.main_

        bot_accs = BotAccounts.bot_usernames
        password = BotAccounts.same_password

        for bots in bot_accs:
            self.browse.get('https://www.instagram.com/accounts/login/')

            sleep(2)

            name_plc = self.browse.find_element(By.Name, 'username')
            passwd_plc = self.browse.find_element(By.Name, 'password')

            name_plc.send_keys(bots)
            passwd_plc.send_keys(password + Keys.ENTER)

            sleep(10)

            for _ in main_acc:
                self.browse.get(f'https://www.instagram.com/{_}')

                sleep(5)

                view_button = self.browse.find_element(By.CLASS_NAME, '_2dbep')

                view_button.click()

                sleep(15)

            self.browse.delete_all_cookies()

        self.browse.quit()


i = InstaBot()


def start_base():
    sleep(2)
    i.login()
    sleep(5)
    print("\nBot Started")
    sleep(2)


# Run by Choice
start = input('''
|-PRESS-------------------|
| 1 - Get who They Follow |
| 2 - Mass Followings     |
| 3 - Send Mass Messages  |
| 4 - Gain Story Views    |
| 5 - Exit                |
|-------------------------|
|-> ''')
sleep(2)


try:
    if start == "1":
        start_base()
        i.get_followings()

    elif start == "2":
        start_base()
        i.follow_page()

    elif start == "3":
        start_base()
        i.message_func()

    elif start == "4":
        start_base()
        i.view_story()

    elif start == "5":
        sleep(2)
        print("\nAlright!!!")
        sys.exit(0)

    else:
        sleep(1)
        print("\nInvalid Input!")
        sys.exit(0)
        
except KeyboardInterrupt:
    print("Alright!!!")
    sys.exit(0)
