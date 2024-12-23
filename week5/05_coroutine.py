import asyncio
import time

def f1():
    print("Start F1")
    time.sleep(2)
    print("End F1")

def f2():
    print("Start F2")
    time.sleep(3)
    print("End F2")

def sync_main():
    print("Start sync main")
    f1()
    f2()
    print("End sync main")

async def c1():
    print("Start C1")
    await asyncio.sleep(2)
    print("End C1")

async def c2():
    print("Start C2")
    await asyncio.sleep(3)
    print("End C2")

async def async_main_inefficient():
    print("Start inefficient_async")
    await c1()
    await c2()
    print("End inefficient_async")

async def async_main_efficient():
    print("Start efficient_async")
    await asyncio.gather(c1(),c2())
    print("End efficient_async")

if __name__ == "__main__":

    start_time = time.time()
    sync_main()
    end_time = time.time()

    print(f"Time taken by sync_main: {(end_time - start_time):.2f} seconds", end="\n\n")

    start_time = time.time()
    asyncio.run(async_main_inefficient())
    end_time = time.time()

    print(f"Time taken by async_main_inefficient: {(end_time - start_time):.2f} seconds", end="\n\n")

    start_time = time.time()
    asyncio.run(async_main_efficient())
    end_time = time.time()

    print(f"Time taken by async_main_efficient: {(end_time - start_time):.2f} seconds", end="\n\n")
