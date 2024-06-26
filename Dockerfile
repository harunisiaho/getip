FROM python:3.12.1-slim-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
