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
    count the call to requests
    """
    redis_conn = redis.Redis()

    @wraps(func)
    def wrapper(url: str) -> str:
        """
        function that will count and cache
        """
        count_key = f"count:{url}"
        cached_key = f"cached:{url}"
        access_count = redis_conn.incr(count_key)
        cached_result = redis_conn.get(cached_key)
        if cached_result:
            return cached_result.decode('utf-8')
        start_time = datetime.now()
        html = func(url)
        end_time = datetime.now()
        redis_conn.setex(cached_key, 10, html)
        response_time = (end_time - start_time).total_seconds()

        return f"Access Count: {access_count}, Response Time:
            {response_time: .4f} seconds, HTML: {html}"

    return wrapper


@count_access
def get_page(url: str) -> str:
    return requests.get(url).text
