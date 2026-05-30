<<<<<<< HEAD
FROM python:3.9
=======
FROM python:3.10-slim
>>>>>>> 604ba2e7481d20ece2c1e9485f87a448df37c2af

WORKDIR /app

COPY . .

<<<<<<< HEAD
RUN pip install flask flask-cors prometheus-flask-exporter

EXPOSE 5000
=======
RUN pip install flask
>>>>>>> 604ba2e7481d20ece2c1e9485f87a448df37c2af

CMD ["python", "app.py"]
