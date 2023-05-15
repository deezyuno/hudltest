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

        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, fname)))

        fn = self.driver.find_element(By.ID, fname)
        fn.send_keys(random.choice(firname))
        ln = self.driver.find_element(By.ID, lname)
        ln.send_keys(random.choice(laname))

        addy = self.driver.find_element(By.ID, email)
        addy.send_keys(email1)

        ph = self.driver.find_element(By.ID, phone)
        ph.send_keys(phone1)

        st = Select(self.driver.find_element(By.ID, state))
        st.select_by_index(random.randint(2, 49))

        co = self.driver.find_element(By.ID, comp)
        co.send_keys(comp1)

        org = Select(self.driver.find_element(By.ID, "organizationLevel_c"))
        org.select_by_index(random.randint(1, 4))

        sp = Select(self.driver.find_element(By.ID, tsport))
        sp.select_by_index(random.randint(1, 35))

        role = Select(self.driver.find_element(By.ID, "Role__c"))
        role.select_by_index(random.randint(1, 13))

        hel = self.driver.find_element(By.ID, mess)
        hel.send_keys(help)

        time.sleep(5)

if __name__ == '__main__':
    # unittest.main(verbosity=2)
    unittest.main()
