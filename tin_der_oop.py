from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class TinderFile:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.__driver = webdriver.Chrome(options=chrome_options)
        self.__driver.get("https://tinder.com/")

        try:
            cookie = self.__driver.find_element(By.XPATH, '//*[@id="q-637390230"]/div/div[2]/div/div/div[1]/div[2]/button/div[2]/div[2]')
            time.sleep(5)
            cookie.click()
            time.sleep(5)
        except Exception as e:
            print(e)

        try:
            login = self.__driver.find_element(By.XPATH, '//*[@id="q-637390230"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
            login.click()
            time.sleep(5)

        except Exception as f:
            print(f)

    def tinder_login(self, fb_mail, fb_password, phone_number):
        """take mail, password and phone number to logged in."""

        self.__mail = fb_mail
        self._pass = fb_password
        self.__phone_num = phone_number

        try:
            login_option = self.__driver.find_element(By.CSS_SELECTOR, ".Expand--s.theme-light button")
            login_option.click()
            time.sleep(5)

            fb_page = self.__driver.find_element(By.XPATH,'//*[@id="q1929195990"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
            fb_page.click()

        except Exception as error:
            print(error)

        try:
            self.__fb_login()

        except Exception as error:
            print(error)

        else:
            print("success")

    def __fb_login(self):

        # self.__driver.maximize_window()
        time.sleep(5)
        base_window = self.__driver.window_handles[0]
        fb_login_window = self.__driver.window_handles[1]

        self.__driver.switch_to.window(fb_login_window)     # switching to fb window
        print(self.__driver.title)
        time.sleep(5)

        fb_mail = self.__driver.find_element(By.XPATH, '//*[@id="email"]')
        fb_mail.send_keys(self.__mail, Keys.TAB, self._pass)
        time.sleep(3)
        fb_mail.send_keys(Keys.ENTER)
        time.sleep(5)

        self.__driver.switch_to.window(base_window)     # switch to tinder window
        print(self.__driver.title)

        try:    # for manual verification.

            while input("have you manually completed verification? type 'yes/no': ").lower() != "yes":
                print("please solve verification manually")

            print("you are successfully logged in.")
            time.sleep(5)

            phone_num = self.__driver.find_element(By.XPATH, '//*[@id="q1929195990"]/main/div/div[1]/div/div[2]/div/div[2]/div')
            phone_num.send_keys(self.__phone_num, Keys.ENTER)

            while input("have you filled your password manually? 'yes/no': ").lower() != "yes":
                print("please fill your code.")
            print("mobile verification successful.")

            time.sleep(10)

            condition_agree = self.__driver.find_element(By.XPATH, '//*[@id="q1929195990"]/main/div/div[1]/button/div[2]')
            condition_agree.click()

        except Exception as e:
            print("Error: if already completed verification than ignore this error.")

