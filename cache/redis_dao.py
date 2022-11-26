import redis
from dataclasses import dataclass
from datetime import datetime
import json

@dataclass
class RedisConfig:
    host : str
    port : int



class RedisManager:
    def __init__(self, conf:RedisConfig) -> None:
        self.conf = conf
        self.client = redis.Redis(host=self.conf.host, port=self.conf.port, password="redis_123")

    def insert(self, key, val, multi=False):
        if not multi:
            self.client.hset(key, val)
        else:
            self.client.mset(mapping={k:v for k,v in zip(key, val)})

    def select(self, key, filters=None, multi=False):
        if not multi:
            if self.client.exists(key):
                try:
                    return self.client.hgetall(key)
                except:
                    return self.client.get(key)
            else:
                raise Exception("Key doesn't exist in cache..")
        else:
            return self.client.mget(keys=key)



cache_manager = RedisManager(conf=RedisConfig(host='127.0.0.1', port=6379))

data = {
    "thread_id" : 1,
    "channel_id" : 1,
    "user_id" : 1,
    "text" : "Hello this is my first msg",
    "created_at" : str(datetime.now())

}

print(cache_manager.select(key="msg4"))

