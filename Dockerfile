# Sử dụng image python chính thức
FROM python:3.9-slim

# Thiết lập biến môi trường
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Thiết lập thư mục làm việc
WORKDIR /code

# Copy requirements.txt và cài đặt các dependency
COPY requirements.txt /code/

# Cập nhật pip trước khi cài đặt các gói
RUN pip install --upgrade pip

# Cài đặt các gói từ requirements.txt với thời gian timeout dài hơn
RUN pip install --default-timeout=100 -r requirements.txt

# Copy toàn bộ mã nguồn vào container
COPY . /code/

# Chạy server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
