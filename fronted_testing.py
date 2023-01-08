from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service("C:/Users/MorHemoELPCNetworksL/Downloads/chromedriver.exe"))


def test_user_name_displayed(user_id):
    # Start a Selenium Webdriver session
    driver = webdriver.Chrome()

    # Navigate to web interface URL using an existing user id
    url = "http://localhost:5001/users/get_user_data/{}".format(user_id)
    driver.get(url)
    time.sleep(3)

    # Check that the user name element is showing
    user_name_element = driver.find_element(by="id", value="user")
    assert user_name_element.is_displayed()

    # Print user name
    print(user_name_element.text)

if __name__ == "__main__":
    test_user_name_displayed(1)