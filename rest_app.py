from flask import Flask, request, jsonify
import os
import signal
import pymysql

app = Flask(__name__)

conn = pymysql.connect(
    host='sql.freedb.tech',
    port=3306,
    user='freedb_DevOps_morhemo',
    password='dJxS8ZQ9y#ACaz2',
    database='freedb_sql.freedb.tech123123'
)
cursor = conn.cursor()

@app.route('/users/<int:user_id>', methods=['POST', 'GET', 'PUT', 'DELETE'])
def handle_user(user_id):
    if request.method == 'POST':
        # Create a new user in the database
        user_name = request.json['user_name']
        query = 'INSERT INTO users (id, name) VALUES (%s, %s)'
        values = (user_id, user_name)
        try:
            cursor.execute(query, values)
            conn.commit()
            return jsonify({'status': 'ok', 'user_added': user_name}), 200
        except pymysql.err.IntegrityError:
            return jsonify({'status': 'error', 'reason': 'id already exists'}), 500
    elif request.method == 'GET':
        query = 'SELECT name FROM users WHERE id = %s'
        values = (user_id,)
        cursor.execute(query, values)
        result = cursor.fetchone()
        if result:
            return jsonify({'status': 'ok', 'user_name': result[0]}), 200
        else:
            return jsonify({'status': 'error', 'reason': 'no such id'}), 500
    elif request.method == 'PUT':
        # Update the user name in the database
        user_name = request.json['user_name']
        query = 'UPDATE users SET name = %s WHERE id = %s'
        values = (user_name, user_id)
        cursor.execute(query, values)
        conn.commit()
        return jsonify({'status': 'ok', 'user_updated': user_name}), 200
    elif request.method == 'DELETE':

        query = 'DELETE FROM users WHERE id = %s'
        values = (user_id,)
        cursor.execute(query, values)
        conn.commit()
        return jsonify({'status': 'ok', 'user_deleted': user_id}), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'
