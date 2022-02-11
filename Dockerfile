FROM python:alpine3.7

# create app directory

WORKDIR /app

# Installing app dependencies using requirements.txt

COPY src/requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source

COPY src /app

EXPOSE 8080

ENV FLASH_ENV dev

CMD ["python", "app.py"]