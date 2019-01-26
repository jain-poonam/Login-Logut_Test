"""
Implement Login/Logout Test for Gmail Application in Android. 
Tool and tests, to automate login and logout
"""
 
import os
import unittest
from appium import webdriver


class GmailAndroidTests(unittest.TestCase):
    "Class to run tests against the Gmail app"
    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = 'Pixel'
        desired_caps['app'] = '/Users/pyjain/Downloads/Gmail-7.3.26.152772569.release.apk'
        desired_caps['appPackage'] = 'com.google.android.gm'
        desired_caps['appActivity'] = 'com.google.android.gm.ui.MailActivityGmail'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
 
    def tearDown(self):
        "Tear down the test"
        self.driver.quit()
   
    def test_mode(self):
        
        file1 = open("/Users/pyjain/Desktop/email_credential.txt").read().splitlines()
        email = file1[0] #Read email id from the given text file 
        pwd = file1[1] #Read password from the given text file
        self.driver.implicitly_wait(90)  #implicitly wait for an element to be found,or a command to complete
        
        "Find element by id and resource id has been generated with the help of  the uiautomatorviewer by taking screenshots"
        element = self.driver.find_element_by_id("com.google.android.gm:id/welcome_tour_got_it")
        element.click() #Clicks the element provided by the id
        
        element = self.driver.find_element_by_id("com.google.android.gm:id/setup_addresses_add_another")
        element.click()
        
        element = self.driver.find_element_by_id("com.google.android.gm:id/account_setup_item")
        element.click()
        
        element = self.driver.find_element_by_id("identifierId")
        element.click()
        
        element.send_keys(email)
        element = self.driver.find_element_by_id("identifierNext")
        element.click()

        element = self.driver.find_element_by_id("password")
        element.click()
       
        element.send_keys(pwd)
        element = self.driver.find_element_by_id("passwordNext")
        element.click()
        
        element = self.driver.find_element_by_id("signinconsentNext")
        element.click()
        
        element = self.driver.find_element_by_id("com.google.android.gms:id/next_button")
        element.click()
        
        element = self.driver.find_element_by_id("com.google.android.gms:id/next_button")
        element.click()
             
        element = self.driver.find_element_by_id("com.google.android.gm:id/account_address")
        element.click()
 
        element = self.driver.find_element_by_id("com.google.android.gm:id/action_done")
        element.click()
         
        element = self.driver.find_element_by_accessibility_id("Open navigation drawer")
        element.click()
        
        element = self.driver.find_element_by_id("com.google.android.gm:id/account_list_button")
        element.click()
         
        element = self.driver.find_element_by_id("com.google.android.gm:id/manage_accounts_text")
        element.click()
         
        element = self.driver.find_element_by_id("com.android.settings:id/icon_frame")
        element.click()
         
        element = self.driver.find_element_by_id("com.android.settings:id/button")
        element.click()
         
        element = self.driver.find_element_by_id("android:id/button1")
        element.click()
        
        
#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GmailAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)