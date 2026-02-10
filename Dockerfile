FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py config.py load_topics.py .
COPY templates/ templates/
COPY static/ static/
COPY topics/ topics/

EXPOSE 5001
CMD ["python", "app.py"]
