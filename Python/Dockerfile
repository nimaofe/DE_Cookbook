
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
