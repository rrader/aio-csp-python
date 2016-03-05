"""
Implementation of CSP on asyncio using custom loop.
"""

import asyncio

from csploop import CSPMasterLoop

async def test():
    i = 0
    while True:
        print(i)
        i += 1


if __name__ == '__main__':
    loop = CSPMasterLoop(slaves_num=1)
    asyncio.set_event_loop(loop)

    asyncio.ensure_future(loop.create_slave_task(test, slave_id=0))

    loop.run_forever()
    loop.close()
