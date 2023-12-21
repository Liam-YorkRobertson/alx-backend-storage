#!/usr/bin/env python3
"""
obtain the HTML content of a particular URL and returns it
"""
import requests
from functools import wraps
from typing import Callable
import redis
from datetime import datetime, timedelta


def count_access(func: Callable) -> Callable:
    """
    count call to requests
    """
    redis_conn = redis.Redis()

    @wraps(func)
    def wrapper(url: str) -> str:
        """
        counts
        """
        count_key = f"count:{url}"
        cached_key = f"cached:{url}"
        access_count = redis_conn.incr(count_key)
        cached_result = redis_conn.get(cached_key)
        if cached_result:
            return cached_result.decode('utf-8')
        html = func(url)
        redis_conn.setex(cached_key, 10, html)
        return f"Access Count: {access_count}, HTML: {html}"
    return wrapper

@count_access
def get_page(url: str) -> str:
    return requests.get(url).text
