FROM python:3.9-slim
RUN pip install Flask
COPY app.py /app/app.py
WORKDIR /app
EXPOSE 5000
CMD ["python", "app.py"]
