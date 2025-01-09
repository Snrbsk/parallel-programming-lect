""" Q2 (25 Points) Write an asynchronous context
manager in Python with the name AsyncFileReader,
which reads the whole content of a file
asynchronously. You can find some codes below to
read a file in synchronous fashion. """

def read_file(filename):
    file = open(filename, mode='r')
    content = file.read()
    file.close()
    return content

def sync_main():
    content = read_file('test.txt')
    print(content)

if __name__ == '__main__':
    sync_main()
    pass

import asyncio
import aiofiles

class AsyncFileReader:
    def __init__(self, file_name):
        self.file_name = file_name
    
    async def __aenter__(self):
        self.file = aiofiles.open(self.file_name,mode='r')
        return self.file
    
    async def __aexit__(self, exc_type, exc, tb):
        await self.file.close()

async def async_main():
    async with AsyncFileReader("test.txt") as file:
        content = await file.read()
        print(content)
        
if __name__ == '__main__':
    asyncio.run(async_main())