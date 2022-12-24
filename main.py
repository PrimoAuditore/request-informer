import os
import redis
import time
import requests

REDIS_HOST = os.environ["REDIS_HOST"]
REDIS_USERNAME = os.environ["REDIS_USERNAME"]
REDIS_PASSWORD = os.environ["REDIS_PASSWORD"]
REDIS_CHANNEL = os.environ["REDIS_CHANNEL"]

redis_con = redis.Redis(host=REDIS_HOST, port=18330, db=0, username=REDIS_USERNAME, password=REDIS_PASSWORD)
pubsub = redis_con.pubsub()

# Subscribe to channel
pubsub.subscribe("test")

while True:
    request_id = pubsub.get_message()
    time.sleep(0.01)
