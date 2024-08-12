FROM python:3.12

WORKDIR /backend

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . ./index-app

CMD ["python", "./index-app/index.py"]

