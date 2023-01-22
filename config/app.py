import json
import flask
import redis

application = flask.Flask(__name__)


def stream_messages(channel):
    r = redis.Redis()
    p = r.pubsub()
    p.subscribe(channel)
    for message in p.listen():
        if message["type"] == "message":
            yield "data: " + json.dumps(message["data"].decode()) + "\n\n"
