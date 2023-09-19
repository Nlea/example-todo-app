# 
FROM python:3.9
WORKDIR /app
COPY . /app 
RUN pip install --no-cache-dir --upgrade -r requirements.txt
EXPOSE 8000
CMD uvicorn main:app --host='::' --port=8000