from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
import accountdetails


class instabot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome(
            executable_path=r"C:\Users\SYDNEY\Downloads\chromedriver_win32 (1)\chromedriver.exe")

        self.driver.get(r"https://www.instagram.com")
        time.sleep(2)
        self.driver.find_element_by_xpath(
            r"/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input") \
            .send_keys(username)
        self.driver.find_element_by_xpath(
            r"/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")\
            .send_keys(pw)
        self.driver.find_element_by_xpath(
            r"/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")\
            .click()
        time.sleep(10)
        self.driver.find_element_by_xpath(
            r"/html/body/div[4]/div/div/div/div[3]/button[2]")\
            .click()

    def _comment_(self,username2,comment) :
        self.driver.find_element_by_xpath(
            r"/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")\
         .send_keys(username2)
        time.sleep(4)
        self.driver.find_element_by_xpath(
            r" /html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[1]/div/div")\
            .click() #this is the problem area
        time.sleep(3)
        self.driver.execute_script(r"window.scrollTo(0,300)")
        time.sleep(2)
        self.driver.find_element_by_xpath(
            r'/html/body/div[1]/section/main/div/div[4]/article/div/div/div[1]/div[1]/a/div[1]/div[2]') \
            .click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            r"/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[2]/button/div/svg")\
            .click()
        self.driver.find_element_by_xpath(
            r"/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea")\
            .send_keys(comment)
        time.sleep(1)
        self.driver.find_element_by_xpath(
            r"/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button[2]")\
            .click()
        time.sleep(5)




if __name__ == '__main__':
    my_bot=instabot(accountdetails.username,accountdetails.password)
    my_bot._comment_("sydney_sk5","bot 1 reporting for duty")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
