"""
Generic implementation of CSP on asyncio.
It has no any advantages since default loop and standard Queue are used.
"""

import asyncio

c = asyncio.Queue(maxsize=1)  # no buffering


async def generate(chan):
    i = 0
    while True:
        await chan.put(i)
        i += 1


async def process(chan):
    while True:
        i = await chan.get()
        print(i)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    asyncio.ensure_future(generate(c))
    asyncio.ensure_future(process(c))

    loop.run_forever()
    loop.close()
