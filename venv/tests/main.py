from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import unittest
# import time
# import datetime
# from datetime import date
import random
from random import randrange
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from resources.generic_elements import *
from selenium.webdriver.support.ui import Select


class HudlProj(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.headless = False
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('https://www.google.com')

    def test_base(self):

        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, gsearch)))
        search = self.driver.find_element(By.XPATH, gsearch)
        search.click()
        search.send_keys("hudl", Keys.ENTER)

        result = self.driver.find_element(By.TAG_NAME,"h3")
        result.click()


        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, rdemo)))
        demo = self.driver.find_element(By.XPATH, rdemo)
        demo.click()

        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, schoollist)))
        hs = self.driver.find_element(By.XPATH, schoollist)
        hs.click()

        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, "FirstName")))

        fn = self.driver.find_element(By.ID, "FirstName")
        fn.send_keys(random.choice(firname))
        ln = self.driver.find_element(By.ID, "LastName")
        ln.send_keys(random.choice(laname))

        addy = self.driver.find_element(By.ID, "Email")
        addy.send_keys(email)

        ph = self.driver.find_element(By.ID, "Phone")
        ph.send_keys(phone)

        st = Select(self.driver.find_element(By.ID, "State"))
        st.select_by_index(random.randint(2, 49))

        co = self.driver.find_element(By.ID, "Company")
        co.send_keys(comp)

        org = Select(self.driver.find_element(By.ID, "organizationLevel_c"))
        org.select_by_index(random.randint(1, 4))

        sp = Select(self.driver.find_element(By.ID, "Team_Sport__c_contact"))
        sp.select_by_index(random.randint(1, 35))

        role = Select(self.driver.find_element(By.ID, "Role__c"))
        role.select_by_index(random.randint(1, 13))

        hel = self.driver.find_element(By.ID, "message_c")
        hel.send_keys(help)



if __name__ == '__main__':
    # unittest.main(verbosity=2)
    unittest.main()
