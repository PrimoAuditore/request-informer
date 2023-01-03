FROM python:3.10-slim-bullseye

ENV REDIS_HOST=""
ENV REDIS_USERNAME=""
ENV REDIS_PASSWORD=""
ENV REDIS_CHANNEL=""
ENV SENTRY_TOKEN=""

COPY . .
RUN pip install -r requirements.txt
CMD ["python", "main.py"]