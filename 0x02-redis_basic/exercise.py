#!/usr/bin/env python3
"""Cache class module"""
import redis
from typing import Union, Callable, Any
import uuid


class Cache:
    """Cach class definition"""
    def __init__(self) -> None:
        """redis initialisation"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """set uuid key"""
        uuid_key = str(uuid.uuid4())
        self._redis.set(uuid_key, data)
        return uuid_key
