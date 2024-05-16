from pathlib import Path
from sys import path
path.append(str(Path(__file__).resolve().parent.parent.parent.absolute()))
from functions import *


def set_config(r, key, value):
    r.set(f"config:{key}", value)


def get_config(r, key):
    value = r.get(f"config:{key}")
    return value.decode('utf-8') if value else None


if __name__ == "__main__":
    r = get_redis_connection()
    set_config("site_name", "My Awesome Site")
    site_name = get_config("site_name")
    print(f"Site name: {site_name}")
