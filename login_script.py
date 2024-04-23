from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to perform login
def perform_login(username, password):
    # Define the URL of the login page
    LOGIN_URL = "https://example.com/login"

    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome('chromedriver.exe')

    # Navigate to the login page
    driver.get(LOGIN_URL)

    # Find the username and password fields and enter the credentials
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")

    username_field.send_keys(username)
    password_field.send_keys(password)

    # Find and click the login button
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    # Wait for the next page to load
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "welcome-message"))
        )
        print("Login successful!")
    except:
        print("Login failed!")

    # Close the browser
    driver.quit()

# Provide the login credentials
USERNAME = "your_username"
PASSWORD = "your_password"

# Call the function to perform the login
perform_login(USERNAME, PASSWORD)

