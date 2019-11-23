import asyncio
from aiohttp import ClientSession

async def long_running_task(sleep_time):
    """Mimicks a long running task"""
    print(f"begin {sleep_time}")
    await asyncio.sleep(sleep_time)
    print(f"awake {sleep_time}")

async def run_task():
    """Function to execute async task"""
    await long_running_task(2)


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with ClientSession() as session:
        html = await fetch(session, 'http://example.com')
        print(html)

if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    asyncio.run(long_running_task(2))