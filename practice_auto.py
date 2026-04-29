import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://parabank.parasoft.com/parabank/index.htm")
list_leftmen_locator = (By.XPATH, "//li[text() = 'Solutions']//parent :: ul//child:: li")
ele_list = driver.find_elements(*list_leftmen_locator)
dict = {}
k = 0
for e in ele_list:
    #print(e.text)
    dict[k] = e.text
    k = k + 1
print(dict)
for k, v in dict.items():
    print(k, ":", v)
log_title_ele = (By.XPATH, "//img[@title = 'ParaBank']")
ele_1 = (driver.find_element(*log_title_ele))
ele_1.click()
#print(ele_1.text)





time.sleep(5000)
