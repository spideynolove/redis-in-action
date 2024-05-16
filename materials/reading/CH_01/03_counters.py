import redis

r = redis.Redis()


def increment_page_hit(page_id):
    r.incr(f"page:{page_id}:hits")


def get_page_hits(page_id):
    hits = r.get(f"page:{page_id}:hits")
    return int(hits) if hits else 0


if __name__ == "__main__":
    page_id = "homepage"
    increment_page_hit(page_id)
    hits = get_page_hits(page_id)
    print(f"Page hits for {page_id}: {hits}")
