import requests
import pymysql

# Set the base URL of the REST API
base_url = 'http://127.0.0.1:5000/users/'

# Set the user ID and user name
user_id = 2
user_name = 'john'

# Set the data for the POST request
data = {'user_name': user_name}

# Send a POST request to the REST API
response = requests.post(base_url + str(user_id), json=data)
print(response.status_code)  # Expected output: 200

# Send a GET request to the REST API
response = requests.get(base_url + str(user_id))
print(response.status_code)  # Expected output: 200
print(response.json())  # Expected output: {'status': 'ok', 'user_name': 'john'}

# Connect to the MySQL database
conn = pymysql.connect(
    host='sql.freedb.tech',
    port=3306,
    user='freedb_DevOps_morhemo',
    password='dJxS8ZQ9y#ACaz2',
    database='freedb_sql.freedb.tech123123'
)
cursor = conn.cursor()

# Query the users table
query = 'SELECT name FROM users WHERE id = %s'
values = (user_id,)
cursor.execute(query, values)
result = cursor.fetchone()
print(result)  # Expected output: ('john',)

conn.close()
