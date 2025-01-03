import asyncio
import time

async def a():
    print("Start A")
    await asyncio.sleep(4)
    print("End A")

async def b():
    print("Start B")
    await asyncio.sleep(2)
    print("End B")

async def c():
    print("Start C")
    await asyncio.sleep(2)
    print("End C")

async def d():
    print("Start D")
    await asyncio.sleep(1)
    print("End D")

async def e():
    print("Start E")
    await asyncio.sleep(1)
    print("End E")

async def f():
    print("Start F")
    await asyncio.sleep(1)
    print("End F")

async def g():
    print("Start G")
    await asyncio.sleep(1)
    print("End G")

async def fg():
    print("Start FG")
    await f()
    await g()
    print("End FG")

async def de():
    print("Start DE")
    await d()
    await e()
    print("End DE")

async def b_de():
    print("Start B_DE")
    await asyncio.gather(b(), de())
    print("End B_DE")

async def c_fg():
    print("Start C_FG")
    await asyncio.gather(c(), fg())
    print("End C_FG")

async def bde_cfg():
    print("Start BDE_CFG")
    await b_de()
    await c_fg()
    print("End BDE_CFG")

async def abcdefg():
    print("Start Main")
    await asyncio.gather(a(), bde_cfg())
    print("End Main")

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(abcdefg())
    end_time = time.time()
    
    print(f"İşlem toplamda {(end_time-start_time):.2f} sn kadar sürdü")