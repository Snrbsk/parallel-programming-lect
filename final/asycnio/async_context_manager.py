""" Q2 (25 Points) Write an asynchronous context
manager in Python with the name AsyncFileReader,
which reads the whole content of a file
asynchronously. You can find some codes below to
read a file in synchronous fashion. """

import asyncio
import aiofiles

class AsyncFileReader:
    def __init__(self, filename):
        self.filename =  filename

    async def __aenter__(self):
        self.file = await aiofiles.open(self.filename, mode="r")
        return self.file

    async def __aexit__(self, exc_type, tb, exc):
        await self.file.close()

async def async_main():
    async with AsyncFileReader("final/asycnio/test.txt") as file:
        content = await file.read()
        print(content)
        
if __name__ == '__main__':
    asyncio.run(async_main())