FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

EXPOSE 8000
WORKDIR /


COPY requirements.txt ./

RUN pip install -r requirements.txt
COPY . ./
CMD ['python', 'bot.py']