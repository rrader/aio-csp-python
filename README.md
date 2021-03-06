Communicating Sequential Processes within Python asyncio env
===========================================================

1. To implement CSP, coroutines should communicate exclusively via channels (queue).
1. Queue should support interprocess communication.
1. Since coroutines do not share memory anymore (except of channels),
they can be executed in separate python processes.
1. It will enable real parallelism since there will be separate GIL in each python process.
1. Ideally there should be same number of parallel loops running as the number of CPU cores <sup>1</sup>.
1. Distributed scheduler should be implemented to coordinate
1. The ability to execute clones of a single coroutine should be present
 (e.g. if the input queue is growing faster then coroutine reads from it).
1. One loop should be "master-loop" that marks coroutines to be executed on specific loop.
1. For the sake of simplicity, initially just round-robin schedule policy should be implemented. 
1. Fast IPC for loops synchronization is required.

-------

**1** There's possibility to implement multi-node parallelism (as in Erlang)

------

References
==================

1. C.A.R. Hoare - Communicating Sequential Processes.
    [Paper](http://spinroot.com/courses/summer/Papers/hoare_1978.pdf).
1. python-csp: implementation of CSP on threads/processes.
    [Code](https://github.com/futurecore/python-csp), [presentation](http://arild.github.io/csp-presentation/).
1. PyCSP: [paper](http://www.wotug.org/paperdb/send_file.php?num=216).
1. aioprocessing - https://github.com/dano/aioprocessing