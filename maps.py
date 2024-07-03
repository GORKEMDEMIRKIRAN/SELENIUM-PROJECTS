



# DOSYA İÇİNE "CHROME,EDGE,MOZILLA" DRIVER EKLEDİM.


from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from selenium.common.exceptions import TimeoutException,WebDriverException,NoSuchElementException

from selenium.webdriver.edge.service import Service as sv_edge
from selenium.webdriver.chrome.service import Service as sv_chrome
from selenium.webdriver.firefox.service import Service as sv_firefox

import time


# 3 FARKLI TARAYICIDA GOOGLE MAPS GİRİŞ YAPTIK.

# Tarayıcılar;   MICROSOFT EDGE, CHROME, FIREFOX

servic_edge=sv_edge(".\\msedgedriver.exe")
driver_edge=webdriver.Edge(service=servic_edge)
driver_edge.get("https://www.google.com/maps")

# servic_chrome=sv_chrome(".\\chromedriver.exe")
# driver_chrome=webdriver.Chrome(service=servic_chrome)
# driver_chrome.get("https://www.google.com/maps")

# servic_firefox=sv_firefox(".\\geckodriver.exe")
# driver_firefox=webdriver.Firefox(service=servic_firefox)
# driver_firefox.get("https://www.google.com/maps")




time.sleep(10)

driver_edge.quit()
