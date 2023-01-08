import pymysql
import datetime

schema_name = "freedb_sql.freedb.tech123123"

# Establishing a connection to DB
conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_DevOps_morhemo', passwd='dJxS8ZQ9y#ACaz2', db=schema_name)
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Create a datetime object for the current date and time
now = datetime.datetime.now()

# Inserting data into table
cursor.execute("CREATE TABLE `"+schema_name+"`.`users`(`id` INT NOT NULL,`name` VARCHAR(45), `creation_time` VARCHAR(45));")

# Inserting data into table

sql = "INSERT into `"+schema_name+"`.`users` (id, name, creation_time) VALUES (1, 'John', %s)"

cursor.execute(sql, (now,))


conn.commit()
conn.close()


