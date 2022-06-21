import asyncio
import aioredis
import os

host = os.environ['REDIS_HOST']
port = os.environ['REDIS_PORT']

async def main():
    KEY = 'my-key'
    VALUE = 'value1'
    # Redis client bound to single connection (no auto reconnection).
    redis = aioredis.from_url(
        f"redis://{host}:{port}", encoding="utf-8", decode_responses=True
    )
    async with redis.client() as conn:
        await conn.set(KEY, VALUE)
        val = await conn.get(KEY)
        assert val == VALUE
        
async def redis_pool():
    KEY = 'my-key'
    VALUE = 'value2'
    # Redis client bound to pool of connections (auto-reconnecting).
    redis = aioredis.from_url(
        f"redis://{host}:{port}", encoding="utf-8", decode_responses=True
    )
    await redis.set(KEY, VALUE)
    val = await redis.get(KEY)
    assert val == VALUE
    
def test_main():
    asyncio.run(main())

def test_redis_pool():
    asyncio.run(redis_pool())

