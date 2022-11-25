import redis
from dataclasses import dataclass

@dataclass
class RedisConfig:
    host : str
    port : int



class RedisManager:
    def __init__(self, conf:RedisConfig) -> None:
        self.conf = conf
        self.client = redis.Redis(host=self.conf.host, port=self.conf.host)


    def insert(self, key, val):
        self.client.set(key, val)

