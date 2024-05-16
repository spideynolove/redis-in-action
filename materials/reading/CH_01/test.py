import redis

# r = redis.Redis()

r = redis.from_url('redis://127.0.0.1:6379/0')
print(r.ping())