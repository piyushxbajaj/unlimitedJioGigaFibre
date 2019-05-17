from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("https://www.jio.com/Jio/portal/myAccount?_afrLoop=66172411470424096&_afrWindowMode=0&_afrWindowId=null#!%40%40%3F_afrWindowId%3Dnull%26_afrLoop%3D66172411470424096%26_afrWindowMode%3D0%26_adf.ctrl-state%3Dmqiv2ap2_63")
elem1 = driver.find_element_by_link_text("Recharge")
elem1.click()

