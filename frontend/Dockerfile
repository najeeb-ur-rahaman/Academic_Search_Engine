FROM python:3.12

WORKDIR /frontend

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . ./flask-app

EXPOSE 8000

CMD ["python", "./flask-app/app.py"]

