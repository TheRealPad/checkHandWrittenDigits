FROM python:3.7

WORKDIR /app

COPY . /app/

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.linux.txt

EXPOSE 8080

CMD ["python", "server/app.py"]