import asyncio, time

'''
a a a a b b b b
c c d d e e f f
g h i j k l m n
'''
async def a():
    await asyncio.sleep(4)

async def b():
    await asyncio.sleep(4)

async def c():
    await asyncio.sleep(2)

async def d():
    await asyncio.sleep(2)

async def e():
    await asyncio.sleep(2)

async def f():
    await asyncio.sleep(2)

async def g():
    await asyncio.sleep(1)

async def h():
    await asyncio.sleep(1)

async def i():
    await asyncio.sleep(1)

async def j():
    await asyncio.sleep(1)

async def k():
    await asyncio.sleep(1)

async def l():
    await asyncio.sleep(1)

async def m():
    await asyncio.sleep(1)

async def n():
    await asyncio.sleep(1)

async def gh():
    await g()
    await h()

async def ij():
    await i()
    await j()

async def kl():
    await k()
    await l()

async def mn():
    await m()
    await n()

async def c_gh():
    await asyncio.gather(c(),gh())

async def d_ij():
    await asyncio.gather(d(),ij())

async def e_kl():
    await asyncio.gather(e(),kl())

async def f_mn():
    await asyncio.gather(f(),mn())

async def cfg_dij():
    await c_gh()
    await d_ij()

async def ekl_fmn():
    await e_kl()
    await f_mn()

async def acfgdij():
    await asyncio.gather(a(),cfg_dij())

async def beklfmn():
    await asyncio.gather(b(),ekl_fmn())

async def main():
    await acfgdij()
    await beklfmn()

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main()) 
    end_time = time.time()

    print(f"Main fonksiyonunun toplam {end_time-start_time} saniye sürdü")