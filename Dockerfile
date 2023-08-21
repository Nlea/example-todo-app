# 
FROM python:3.9


WORKDIR /app
COPY ./app 


COPY ./requirements.txt /code/requirements.txt
 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


CMD uvicorn main:app --host='::' --port=$PORT