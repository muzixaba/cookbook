import asyncio
from aiohttp import ClientSession

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with ClientSession() as session:
        html = await fetch(session, 'http://examle.com')
        print(html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())