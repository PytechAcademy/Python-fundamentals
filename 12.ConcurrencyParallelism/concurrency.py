import asyncio

async def fetch_url(url):
    print(f"Fetching {url}")
    await asyncio.sleep(2)
    print(f"Fetched {url}")

async def main():
    await asyncio.gather(fetch_url("url1"), fetch_url("url2"))

asyncio.run(main())