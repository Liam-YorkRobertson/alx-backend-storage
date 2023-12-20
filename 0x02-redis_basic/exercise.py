#!/usr/bin/env python3
"""
Working with the basic aspects of redis
"""
import redis
import uuid


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

    def store(self, data) -> str:
        """
        store input data in Redis
        """
        gen_key = str(uuid.uuid4())
        self._redis.set(gen_key, data)
        return (gen_key)
