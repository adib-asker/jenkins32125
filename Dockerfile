FROM python:3.10

WORKDIR /src

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python3.10", "manage.py", "runserver", "0.0.0.0:8000"]

# sudo docker build -t <image_name>:<tag> .

# sudo docker run -p 8000:8000 <image_name>:<tag>