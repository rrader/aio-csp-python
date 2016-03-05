import importlib
import multiprocessing
import asyncio

import aioprocessing

from csploop import CSPSlaveLoop


class Slave:
    def __init__(self):
        self._coro_queue = aioprocessing.AioQueue()
        self._loop = CSPSlaveLoop()
        self._process = multiprocessing.Process(target=self.main)
        self._process.start()

    def main(self):
        """
        Main function of the slave
        """
        asyncio.set_event_loop(self._loop)
        self._loop.create_task(self.scheduler())
        self._loop.run_forever()
        self._loop.close()

    async def scheduler(self):
        while True:
            coro_spec = await self._coro_queue.coro_get()

            module = importlib.import_module(coro_spec['module'])
            coro = getattr(module, coro_spec['name'])
            self._loop.create_task(coro(*coro_spec['args'], **coro_spec['kwargs']))

    async def create_task(self, coro, args, kwags):
        await self._coro_queue.coro_put({'module': coro.__module__,
                                         'name': coro.__name__,
                                         'args': args,
                                         'kwargs': kwags
                                         })
