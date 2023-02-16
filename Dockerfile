FROM python:3.9-alpine

RUN mkdir /app
WORKDIR /app

COPY hello_world.py .
COPY IF.txt .
COPY Limerick.txt .

#CMD [ "python", "app.py" ]
CMD [ "sh", "-c", "python /app/hello_world.py && cat /app/result.txt" ]