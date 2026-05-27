FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install flask flask-cors prometheus-flask-exporter

EXPOSE 5000

CMD ["python", "app.py"]
