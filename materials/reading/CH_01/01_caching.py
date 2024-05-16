from pathlib import Path
from sys import path
path.append(str(Path(__file__).resolve().parent.parent.parent.absolute()))
from functions import *
import requests


def fetch_url(url):
    r = get_redis_connection()
    root_domain = get_root_domain(url)
    cached_content = r.get(root_domain)
    if cached_content:
        print("Cache hit")
        return cached_content

    print("Cache miss")
    response = requests.get(url)
    r.setex(root_domain, 360, response.content)
    return response.content


if __name__ == "__main__":
    url = "https://redis-py.readthedocs.io/"
    content = fetch_url(url)
    print(content)
