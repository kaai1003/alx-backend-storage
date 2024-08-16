#!/usr/bin/env python3
"""Cache class module"""
from functools import wraps
from typing import Union, Callable, Any
import redis
import uuid


def count_calls(method: Callable) -> Callable:
    """increments the count for that key
    every time the method is called
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> str:
        """wrapper function"""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """store the history of inputs and outputs"""
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> str:
        """wrapper function"""
        self._redis.rpush(f'{method.__qualname__}:inputs', str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(f'{method.__qualname__}:outputs', result)
        return result
    return wrapper


class Cache:
    """Cach class definition"""
    def __init__(self) -> None:
        """redis initialisation"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """set uuid key"""
        uuid_key = str(uuid.uuid4())
        self._redis.set(uuid_key, data)
        return uuid_key

    def get(self, key: str,
            fn: Callable = None) -> Any:
        """convert the data back to the desired format"""
        data = self._redis.get(key)
        if data is None:
            return
        if fn is None:
            return data
        return fn(data)

    def get_str(self, data: str) -> str:
        """str conversion function"""
        return data.decode('utf-8')

    def get_int(self, data: str) -> int:
        return int(data)
