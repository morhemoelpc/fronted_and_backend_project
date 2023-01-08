import time
import datetime
import requests
import pymysql
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set the path to the ChromeDriver executable
chrome_driver_path = 'C:/devops/Project/chromedriver.exe'

# Create a ChromeOptions object to specify additional options for the ChromeDriver
chrome_options = Options()
chrome_options.add_argument(f"--driver-path={chrome_driver_path}")

# Set the base URL of the REST API
base_url = 'http://127.0.0.1:5000/users/'

# Set the user ID and user name
user_id = 2
user_name = 'john'

# Set the data for the POST request
data = {'user_name': user_name}

# Send a POST request to the REST API to create a new user
response = requests.post(base_url + str(user_id), json=data)

# Check that the POST request was successful
if response.status_code != 200:
    raise Exception("Failed to create new user via REST API")

# Send a GET request to the REST API to retrieve the user data
response = requests.get(base_url + str(user_id))

# Check that the GET request was successful and that the user data is correct
if response.status_code != 200 or response.json()['user_name'] != user_name:
    raise Exception("Failed to retrieve user data via REST API")

# Connect to the MySQL database
conn = pymysql.connect(
    host='sql.freedb.tech',
    port=3306,
    user='freedb_DevOps_morhemo',
    password='dJxS8ZQ9y#ACaz2',
    database='freedb_sql.freedb.tech123123'
)
cursor = conn.cursor()


# Query the users table to check that the new user was added to the database
query = 'SELECT name FROM users WHERE id = %s'
values = (user_id,)
cursor.execute(query, values)
result = cursor.fetchone()
if result is None or result[0] != user_name:
    raise Exception("Failed to retrieve user data from database")

# Close the database connection
conn.close()

# Start a Selenium WebDriver session
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the web interface URL using the new user id
url = "http://localhost:5001/users/get_user_data/{}".format(user_id)
driver.get(url)
time.sleep(3)

# Check that the user name is correct
user_element = driver.find_element(by="id", value="user")
assert user_element.is_displayed()
if user_element.text != user_name:
    raise Exception("Web interface returned incorrect user name")


# Close the Selenium Webdriver session
driver.close()

print("All checks pass.")
