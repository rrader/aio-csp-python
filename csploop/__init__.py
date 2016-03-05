from asyncio import SelectorEventLoop


class CSPMasterLoop(SelectorEventLoop):
    def __init__(self, slaves_num):
        super().__init__()
        self.slaves = [Slave() for _ in range(slaves_num)]

    @property
    def slaves_num(self):
        return len(self.slaves)

    async def create_slave_task(self, coro, slave_id, *args, **kwags):
        await self.slaves[slave_id].create_task(coro, args, kwags)


class CSPSlaveLoop(SelectorEventLoop):
    def __init__(self):
        super().__init__()

from csploop.slave import Slave
