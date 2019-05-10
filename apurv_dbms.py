import sqlite3
conn = sqlite3.connect('X.db')

#sql = "CREATE TABLE XYZ(NAME varchar(20), AGE int)"
#conn.execute(sql)
#conn.commit()

sql = "INSERT INTO XYZ(NAME,AGE) VALUES ('Sudeep',18),('Apurv',19),('Ashish',19),('Aman',19),('Divyanshu',19),('Krishna',19)"
conn.execute(sql)
conn.commit()

sql = "SELECT * FROM XYZ"
conn.execute(sql)
conn.commit()
cur = conn.cursor()
cur.execute(sql)
results = cur.fetchall()

print(results)

#sql = "UPDATE XYZ SET AGE = AGE+10"
#conn.execute(sql)
#conn.commit()
#sql = "SELECT * FROM XYZ"
#conn.execute(sql)
#conn.commit()
#cur = conn.cursor()
#cur.execute(sql)
#results = cur.fetchall()
#print(results)

sql = "DELETE FROM XYZ WHERE AGE = 18"
#sql = "DELETE FROM XYZ"
conn.execute(sql)
conn.commit()

sql = "SELECT * FROM XYZ"
conn.execute(sql)
conn.commit()
cur = conn.cursor()
cur.execute(sql)
results = cur.fetchall()
print(results)
