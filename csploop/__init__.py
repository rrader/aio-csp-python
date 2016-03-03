import socket
import subprocess
from asyncio import AbstractEventLoop


class CSPLoop(AbstractEventLoop):
    def call_later(self, delay, callback, *args):
        pass

    def run_in_executor(self, executor, func, *args):
        pass

    def close(self):
        pass

    def get_debug(self):
        pass

    def sock_sendall(self, sock, data):
        pass

    def run_forever(self):
        pass

    def get_task_factory(self):
        pass

    def getaddrinfo(self, host, port, *, family=0, type=0, proto=0, flags=0):
        pass

    def sock_accept(self, sock):
        pass

    def add_signal_handler(self, sig, callback, *args):
        pass

    def getnameinfo(self, sockaddr, flags=0):
        pass

    def add_reader(self, fd, callback, *args):
        pass

    def set_default_executor(self, executor):
        pass

    def call_exception_handler(self, context):
        pass

    def run_until_complete(self, future):
        pass

    def sock_recv(self, sock, nbytes):
        pass

    def is_running(self):
        pass

    def is_closed(self):
        pass

    def _timer_handle_cancelled(self, handle):
        pass

    def create_datagram_endpoint(self, protocol_factory, local_addr=None, remote_addr=None, *, family=0, proto=0,
                                 flags=0, reuse_address=None, reuse_port=None, allow_broadcast=None, sock=None):
        pass

    def time(self):
        pass

    def connect_write_pipe(self, protocol_factory, pipe):
        pass

    def subprocess_exec(self, protocol_factory, *args, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE, **kwargs):
        pass

    def remove_writer(self, fd):
        pass

    def call_at(self, when, callback, *args):
        pass

    def create_connection(self, protocol_factory, host=None, port=None, *, ssl=None, family=0, proto=0, flags=0,
                          sock=None, local_addr=None, server_hostname=None):
        pass

    def sock_connect(self, sock, address):
        pass

    def set_task_factory(self, factory):
        pass

    def set_debug(self, enabled):
        pass

    def set_exception_handler(self, handler):
        pass

    def create_server(self, protocol_factory, host=None, port=None, *, family=socket.AF_UNSPEC, flags=socket.AI_PASSIVE,
                      sock=None, backlog=100, ssl=None, reuse_address=None, reuse_port=None):
        pass

    def remove_reader(self, fd):
        pass

    def create_task(self, coro):
        pass

    def connect_read_pipe(self, protocol_factory, pipe):
        pass

    def create_unix_connection(self, protocol_factory, path, *, ssl=None, sock=None, server_hostname=None):
        pass

    def remove_signal_handler(self, sig):
        pass

    def create_unix_server(self, protocol_factory, path, *, sock=None, backlog=100, ssl=None):
        pass

    def default_exception_handler(self, context):
        pass

    def subprocess_shell(self, protocol_factory, cmd, *, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, **kwargs):
        pass

    def call_soon_threadsafe(self, callback, *args):
        pass

    def add_writer(self, fd, callback, *args):
        pass

    def stop(self):
        pass

