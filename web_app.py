from flask import Flask, request
import pymysql

app = Flask(__name__)

# Connect to the MySQL database
conn = pymysql.connect(
    host='sql.freedb.tech',
    port=3306,
    user='freedb_DevOps_morhemo',
    password='dJxS8ZQ9y#ACaz2',
    database='freedb_sql.freedb.tech123123'
)
cursor = conn.cursor()

@app.route("/users/get_user_data/<int:user_id>")
def get_user_data(user_id):
    # Query the users table to get the user name
    query = 'SELECT name FROM users WHERE id = %s'
    values = (user_id,)
    cursor.execute(query, values)
    result = cursor.fetchone()
    if result is not None:
        # Return the user name as HTML
        return f"<html><body><h1 id='user'>{result[0]}</h1></body></html>"
    else:
        # Return an error message as HTML
        return f"<html><body><h1 id='error'>No such user: {user_id}</h1></body></html>"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
