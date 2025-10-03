import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

service = ChromeService(executable_path = ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# login
driver.get("https://utexas.campuslabs.com/engage/actioncenter/branch/uta/Registrations/RegistrationSubmissionsForExistingGroups/666165?backUrl=https%3A%2F%2Futexas.campuslabs.com%2Fengage%2Factioncenter%2Fbranches%2FUTA%2Fregistrations")
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("USERNAME") # CHANGED for privacy

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("PASSWORD") # CHANGED for privacy

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

# authenticate within 25s
time.sleep(20)

# dropdown: pending -> denied
status_dropdown = driver.find_element(By.ID, "SubmissionStatus")
select = Select(status_dropdown)
select.select_by_visible_text("Denied")

time.sleep(5)

# click on eye button (for loop)
denial_list = []
entries = driver.find_elements(By.CLASS_NAME, "icon-eye")
for entry in entries:
    entry.click()

    # scrape the comment text (adjust selector based on actual HTML structure)
    try:
        comment_element = driver.find_element(By.CLASS_NAME, "comment")  
        comment = comment_element.text
    except:
        comment = "No comment found" # should not happen

    denial_list.append(comment)

    time.sleep(5)
    # go back

print(denial_list)

driver.quit()
