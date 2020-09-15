from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import smtplib

class search:
    def __init__(self, data):
        self.driver = webdriver.Firefox()
        self.driver.get("https://enabiz.gov.tr")
        self.data = data