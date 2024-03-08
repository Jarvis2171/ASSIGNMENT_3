from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the Chrome webdriver
driver = webdriver.Chrome()

# Open Instagram
driver.get("https://www.instagram.com/")

# Wait for the page to load
wait = WebDriverWait(driver, 50)
wait.until(EC.presence_of_element_located((By.NAME, "username")))

username_input = driver.find_element("name", "username")
password_input = driver.find_element("name", "password")

username_input.send_keys("dead_end.____")
password_input.send_keys("Mark2171.")
password_input.send_keys(Keys.ENTER)

# Wait for the login to complete
wait.until(EC.url_changes("https://www.instagram.com/"))


not_now_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div")))
not_now_button.click()

# Wait for the "Not Now" button to become stale
wait.until(EC.staleness_of(not_now_button))

# Find the "Not Now" button again
not_now_button2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]")))
not_now_button2.click()


# Wait for the home page to load
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))

# Search for "msdhoni"
search_box = driver.find_element(By.XPATH, '//input[@placeholder="Search"]')
search_box.send_keys("msdhoni")

# Wait for the search results to load
time.sleep(50)

# Click on the first search result (usually the user's account)
first_result = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div[1]/nav/div/header/div/div/div[1]/div/div/div/div/div/div[3]/div/div/div/div/div/div/div/a[1]/div[1]")))
first_result.click()
driver.quit()
