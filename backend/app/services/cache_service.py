import hashlib
import json

class CacheService:
    def __init__(self):
        self.cache = {}

    def make_key(self, payload: dict) -> str:
        payload_string = json.dumps(payload, sort_keys=True)
        return hashlib.sha256(payload_string.encode()).hexdigest()

    def get(self, key: str):
        return self.cache.get(key)

    def set(self, key: str, value: dict):
        self.cache[key] = value
