FROM python:3.8.12-slim

COPY requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app
COPY app /app

EXPOSE 8080

ENTRYPOINT ["python"]
CMD ["main.py"]