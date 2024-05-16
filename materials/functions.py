import redis
from urllib.parse import urlparse


def get_redis_connection():
    try:
        r = redis.Redis()
        r.ping()
        return r
    except redis.ConnectionError as e:
        return f"Error connecting to Redis: {e}"


def get_root_domain(url):
    return urlparse(url).netloc.split('.')[0]
