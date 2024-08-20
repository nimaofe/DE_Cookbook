
# کتابخانه راهنمای مهندسی داده

این پروژه شامل مثال‌های پایتونی برای مهندسی داده در یک کسب‌وکار با برنامه‌های تحت وب، داکر و سرورهای آپاچی می‌باشد.
----
 پایتون برای مهندسی داده برای یک کسب‌وکار که برنامه‌های تحت وب دارند و از داکر و سرورهای آپاچی استفاده می‌کنند، می‌تواند شامل موضوعات زیر باشد:

1. **مبانی پایتون**:
    - معرفی پایتون
    - متغیرها و انواع داده‌ها
    - عملگرها
    - ساختارهای کنترلی (حلقه‌ها و شرط‌ها)
    - توابع
    - ماژول‌ها و کتابخانه‌ها

2. **کتابخانه‌های مهم برای مهندسی داده**:
    - `pandas` برای کار با داده‌های جدولی
    - `numpy` برای محاسبات عددی
    - `matplotlib` و `seaborn` برای بصری‌سازی داده‌ها

3. **پایگاه‌های داده**:
    - اتصال به پایگاه داده (مثلاً `PostgreSQL` یا `MySQL`)
    - انجام عملیات‌های CRUD (Create, Read, Update, Delete)

4. **ایجاد API با فریم‌ورک `Flask`**:
    - نصب و راه‌اندازی Flask
    - ایجاد روت‌ها و هندلرها
    - کار با JSON

5. **کار با داکر**:
    - نصب و راه‌اندازی داکر
    - ایجاد Dockerfile
    - ساخت و اجرای کانتینرها

6. **استفاده از سرور آپاچی**:
    - تنظیمات اولیه آپاچی
    - دیپلوی کردن برنامه‌ی پایتون با استفاده از WSGI

### 1. مبانی پایتون

#### معرفی پایتون
پایتون یک زبان برنامه‌نویسی سطح بالا و همه‌منظوره است که برای کاربردهای مختلفی از جمله مهندسی داده، توسعه وب و هوش مصنوعی استفاده می‌شود.

#### متغیرها و انواع داده‌ها

```python
# متغیرها
اسم = "علی"
سن = 25
وزن = 70.5
متاهل = False

# چاپ متغیرها
print(f"اسم: {اسم}")
print(f"سن: {سن}")
print(f"وزن: {وزن}")
print(f"متاهل: {متاهل}")
```

#### عملگرها

```python
# عملگرهای ریاضی
جمع = 10 + 5
تفریق = 10 - 5
ضرب = 10 * 5
تقسیم = 10 / 5

print(f"جمع: {جمع}, تفریق: {تفریق}, ضرب: {ضرب}, تقسیم: {تقسیم}")

# عملگرهای منطقی
x = 10
y = 5
print(x > y)  # True
print(x < y)  # False
```

#### ساختارهای کنترلی

```python
# شرط‌ها
سن = 20
if سن >= 18:
    print("بزرگسال")
else:
    print("کودک")

# حلقه‌ها
for i in range(5):
    print(i)

i = 0
while i < 5:
    print(i)
    i += 1
```

#### توابع

```python
def جمع_اعداد(a, b):
    return a + b

نتیجه = جمع_اعداد(5, 10)
print(f"نتیجه جمع: {نتیجه}")
```

### 2. کتابخانه‌های مهم برای مهندسی داده

#### `pandas` برای کار با داده‌های جدولی

```python
import pandas as pd

# ایجاد DataFrame
data = {
    'نام': ['علی', 'مریم', 'نیما'],
    'سن': [25, 30, 22],
    'شهر': ['تهران', 'اصفهان', 'مشهد']
}
df = pd.DataFrame(data)

# نمایش داده‌ها
print(df)

# محاسبه میانگین سن
میانگین_سن = df['سن'].mean()
print(f"میانگین سن: {میانگین_سن}")
```

#### `numpy` برای محاسبات عددی

```python
import numpy as np

# ایجاد آرایه
آرایه = np.array([1, 2, 3, 4, 5])

# انجام محاسبات
جمع = np.sum(آرایه)
میانگین = np.mean(آرایه)

print(f"جمع آرایه: {جمع}")
print(f"میانگین آرایه: {میانگین}")
```

#### `matplotlib` و `seaborn` برای بصری‌سازی داده‌ها

```python
import matplotlib.pyplot as plt
import seaborn as sns

# رسم نمودار
plt.plot([1, 2, 3, 4], [10, 20, 25, 30])
plt.xlabel('محور X')
plt.ylabel('محور Y')
plt.title('نمودار خطی')
plt.show()

# رسم نمودار با Seaborn
sns.barplot(x=['علی', 'مریم', 'نیما'], y=[25, 30, 22])
plt.xlabel('نام')
plt.ylabel('سن')
plt.title('نمودار ستونی')
plt.show()
```

### 3. پایگاه‌های داده

#### اتصال به پایگاه داده

```python
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
```

### 4. ایجاد API با فریم‌ورک `Flask`

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/v1/users', methods=['GET'])
def get_users():
    users = [
        {'id': 1, 'name': 'علی'},
        {'id': 2, 'name': 'مریم'}
    ]
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
```

### 5. کار با داکر

#### ایجاد Dockerfile

```
# استفاده از تصویر پایه پایتون
FROM python:3.8-slim-buster

# تنظیم دایرکتوری کاری
WORKDIR /app

# کپی فایل‌های مورد نیاز به کانتینر
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

# اجرا کردن اپلیکیشن
CMD ["python", "app.py"]
```

#### ساخت و اجرای کانتینرها

```sh
# ساخت تصویر داکر
docker build -t myapp .

# اجرای کانتینر
docker run -d -p 5000:5000 myapp
```

### 6. استفاده از سرور آپاچی

#### تنظیمات اولیه آپاچی

فرض کنید از WSGI برای اجرای اپلیکیشن پایتونی استفاده می‌کنیم.

**فایل `myapp.wsgi`:**

```python
import sys
sys.path.insert(0, '/path/to/your/app')

from app import app as application
```

#### تنظیمات آپاچی برای اجرای اپلیکیشن

**فایل پیکربندی آپاچی `myapp.conf`:**

```
<VirtualHost *:80>
    ServerName myapp.com

    WSGIDaemonProcess myapp python-path=/path/to/your/app
    WSGIScriptAlias / /path/to/your/app/myapp.wsgi

    <Directory /path/to/your/app>
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/myapp_error.log
    CustomLog ${APACHE_LOG_DIR}/myapp_access.log combined
</VirtualHost>
```

