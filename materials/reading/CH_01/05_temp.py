from pathlib import Path
from sys import path
path.append(str(Path(__file__).resolve().parent.parent.parent.absolute()))
from functions import *


def create_temp_token(r, token, value, ttl):
    r.setex(token, ttl, value)


def get_temp_token(r, token):
    value = r.get(token)
    return value.decode('utf-8') if value else None


if __name__ == "__main__":
    r = get_redis_connection()
    token = "temp_token_123"
    value = "some_temporary_value"
    ttl = 180  
    create_temp_token(r, token, value, ttl)
    retrieved_value = get_temp_token(r, token)
    print(f"Retrieved token value: {retrieved_value}")
