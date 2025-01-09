#async with prime

import asyncio
import aiohttp

async def get_primes_below(number: int, session: aiohttp.ClientSession)->list:
    print("Getting primes below {number}")
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6)"
        "AppleWebKit/537.36 (KHTML, like Gecko)"
        "Chrome/106.0.0.0 Safari/537.36"
    }

    url = f"https://www.canbula.com/prime/{number}"
    async with session.get(url, headers= headers, ssl=None) as response:
        primes = (await response.json())["primes"]
    print(f"Got primes below {number}: {primes}")
    return primes

async def scheduling(numbers : list):
    async with aiohttp.ClientSession() as session:        
        objects = [get_primes_below(n, session) for n in numbers]
        await asyncio.gather(*objects)

if __name__ == "__main__":
    asyncio.run(scheduling([50,10,30,40,20]))