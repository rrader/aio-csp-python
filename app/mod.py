"""
Implementation of CSP on asyncio using custom loop.
"""

import asyncio

from csploop import CSPLoop

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
    loop = CSPLoop()
    asyncio.set_event_loop(loop)

    asyncio.ensure_future(generate(c))
    asyncio.ensure_future(process(c))

    loop.run_forever()
    loop.close()
