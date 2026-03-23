FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY templates templates/

VOLUME /data

ENV NOTES_FILE=/data/notes.json
ENV APP_NAME="Docker Notes App"

EXPOSE 5000

ENTRYPOINT ["python", "app.py"]
