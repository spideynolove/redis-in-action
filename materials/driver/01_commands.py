import redis
r = redis.Redis(decode_responses=True)

# print(r.ping())

r.set('name', 'Hung')
print(r.get('name'))
# print(r.get('addr'))
