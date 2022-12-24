FROM python:3.9.6

ENV REDIS_HOST=redis-18330.c289.us-west-1-2.ec2.cloud.redislabs.com
ENV REDIS_USERNAME=default
ENV REDIS_PASSWORD=YSapXsE2qWYiE3f1UThOVfveQq7FSucQ


COPY . .
RUN pip install -r requirements.txt
CMD ["python", "main.py"]