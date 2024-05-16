import redis
import json

r = redis.Redis()


def create_session(session_id, user_data):
    r.setex(f"session:{session_id}", 180, json.dumps(user_data))


def get_session(session_id):
    session_data = r.get(f"session:{session_id}")
    return json.loads(session_data) if session_data else None


if __name__ == "__main__":
    session_id = "abc123"
    user_data = {"user_id": 1, "username": "hung_nguyen"}
    create_session(session_id, user_data)
    session = get_session(session_id)
    print(f"Session data: {session}")
