#!/usr/bin/env python3
"""
Working with the basic aspects of redis
"""
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """
    working with Redis as a cache
    """
    def __init__(self):
        """
        initializing instance and flushing it
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store input data in Redis
        """
        gen_key = str(uuid.uuid4())
        self._redis.set(gen_key, data)
        return (gen_key)

    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int]:
        value = self._redis.get(key)
        if fn is not None:
            return fn(value)
        else:
            return value

    def get_str(self, key: str) -> str:
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        return self.get(key, fn=int)