FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update
RUN apt-get install -y wait-for-it

# RUN apt-get install -y supervisor

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 8000 5432

CMD [ "./run.sh" ]

# EXPOSE 6379 # Redis

# CMD [ "/usr/bin/supervisord", "-c", "supervisord.conf" ]
