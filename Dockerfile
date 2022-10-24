FROM python:3.10 as base

RUN mkdir /app 

COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

FROM base as app

COPY ./code /app/

EXPOSE 8000

WORKDIR /app

ENTRYPOINT [ "python", "manage.py", "runserver" ]