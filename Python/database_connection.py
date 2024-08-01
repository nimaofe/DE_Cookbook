
# اتصال به پایگاه داده

import psycopg2

# اتصال به پایگاه داده
conn = psycopg2.connect(
    dbname='testdb',
    user='testuser',
    password='testpass',
    host='localhost'
)

# ایجاد cursor
cur = conn.cursor()

# اجرای یک کوئری
cur.execute("SELECT * FROM users")

# دریافت نتایج
نتایج = cur.fetchall()

# بستن ارتباط
cur.close()
conn.close()

# نمایش نتایج
for row in نتایج:
    print(row)
