import functools


def cached(cache):
    def decorator(func):
        @functools.wraps(func)
        async def _inner(*args, **kwargs):
            key = func.__name__
            res = await cache.get(key, (args, kwargs))
            if res:
                print('using cache: {}'.format(res))
            else:
                print('cache miss')
                res = func(*args, **kwargs)
                await cache.set(key, res, (args, kwargs))
            return res
        return _inner
    return decorator
