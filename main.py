import os
import redis
import time
import json
import requests
import sentry_sdk

REDIS_HOST = os.environ["REDIS_HOST"]
REDIS_USERNAME = os.environ["REDIS_USERNAME"]
REDIS_PASSWORD = os.environ["REDIS_PASSWORD"]
REDIS_CHANNEL = os.environ["REDIS_CHANNEL"]
SENTRY_DSN = os.environ["SENTRY_DSN"]

print(os.environ)

sentry_sdk.init(
    dsn=SENTRY_DSN,
    traces_sample_rate=1.0
)


class MessageLog:
    timestamp = "",
    phone_number = "",
    origin = "",
    register_id = "",
    destination_systems = []


def get_redis_con():
    return redis.Redis(host=REDIS_HOST, port=18330, db=0, username=REDIS_USERNAME, password=REDIS_PASSWORD)


def subscribe_channel():
    con = get_redis_con()

    pubsub = con.pubsub()
    pubsub.psubscribe(REDIS_CHANNEL)

    return pubsub


def get_system_webhook(system_id):
    con = get_redis_con()
    return con.get("system-webhook:" + str(system_id))


def parse_log(json_log):
    print(json_log)
    log = MessageLog()
    print(json_log["origin"])
    log.origin = json_log["origin"]
    log.timestamp = json_log["timestamp"]
    log.phone_number = json_log["phone_number"]
    log.register_id = json_log["register_id"]
    log.destination_systems = json_log["destination_systems"]

    return log


def execute_request(log, webhook):
    payload = {'origin': log.origin, 'timestamp': log.timestamp, 'destination_systems': log.destination_systems,
               'phone_number': log.phone_number, 'register_id': log.register_id}

    try:
        requests.post(webhook, data=payload)
    except Exception as e:
        sentry_sdk.capture_exception(e)


def message_handler(log):
    # If it's a user sent message
    if log.origin == "INCOMING":
        for system in log.destination_systems:
            webhook = get_system_webhook(system)

            if webhook is not None:
                execute_request(log, webhook)


sub_con = subscribe_channel()

while True:
    message_log = sub_con.get_message()
    if message_log is not None and message_log["type"] == "pmessage":
        log = parse_log(json.loads(message_log["data"]))
        message_handler(log)

    time.sleep(0.01)
