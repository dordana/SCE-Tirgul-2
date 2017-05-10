from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from app import app

class AppTestCae(unittest.TestCase):


    def test_Manager_Option(self):
        #../tests/chromedriver
        ################# Get In with correct details #################
        browser = webdriver.Chrome()
        browser.get('http://127.0.0.1:5000/')
        first_name_Input = browser.find_element_by_id("first_name")
        first_name_Input.send_keys("lilo")
        last_name_Input = browser.find_element_by_id("last_name")
        last_name_Input.send_keys("siksik")
        id_Input = browser.find_element_by_id("user_id")
        id_Input.send_keys("66")
        id_Input.send_keys(Keys.ENTER)
        #browser.save_screenshot('correctDatails.png')
        browser.close()

    def test_missing_id_(self):
        ################# Try to Get In with incorrect details ##########
        browser = webdriver.Chrome()
        browser.get('http://127.0.0.1:5000/')
        first_name_Input = browser.find_element_by_id("first_name")
        first_name_Input.send_keys("lilo")
        last_name_Input = browser.find_element_by_id("last_name")
        last_name_Input.send_keys("horesh")
        id_Input = browser.find_element_by_id("user_id")
        id_Input.send_keys("66")
        id_Input.send_keys(Keys.ENTER)
        #browser.save_screenshot('incorrectDatails.png')
        browser.close()
        #################################################################


if __name__ == '__main__':
    unittest.main()


#################################################################

# from tkinter import Image
#
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# ################# Get In with correct details #################
#
# chromedriver = "../tests/chromedriver"
# browser = webdriver.Chrome()
# browser.get('http://127.0.0.1:5000/')
# first_name_Input = browser.find_element_by_id("first_name")
# first_name_Input.send_keys("lilo")
# last_name_Input = browser.find_element_by_id("last_name")
# last_name_Input.send_keys("siksik")
# id_Input =  browser.find_element_by_id("user_id")
# id_Input.send_keys("66")
# id_Input.send_keys(Keys.ENTER)
# browser.save_screenshot('correctDatails.png')
# browser.close()
# #################################################################
#
# ################# Try to Get In with incorrect details ##########
#
# browser = webdriver.Chrome()
# browser.get('http://127.0.0.1:5000/')
# first_name_Input = browser.find_element_by_id("first_name")
# first_name_Input.send_keys("lilo")
# last_name_Input = browser.find_element_by_id("last_name")
# last_name_Input.send_keys("horesh")
# id_Input =  browser.find_element_by_id("user_id")
# id_Input.send_keys("66")
# id_Input.send_keys(Keys.ENTER)
# browser.save_screenshot('incorrectDatails.png')
# browser.close()
# #################################################################
#
#
#
#