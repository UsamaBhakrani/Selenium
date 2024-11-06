from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=options)

driver.get("https://github.com")

sign_in = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in.click()

email = driver.find_element(by=By.ID, value="login_field")
email.send_keys("")

password = driver.find_element(by=By.ID, value="password")
password.send_keys("")

sign_in_button = driver.find_element(by=By.NAME, value="commit")
sign_in_button.click()

driver.implicitly_wait(5.0)

avatar_circle = driver.find_element(by=By.CLASS_NAME, value="avatar circle")
avatar_circle.click()


# repositories = driver.find_element(by=By.ID, value=':rf:')
# repositories.click()
