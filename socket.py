import socket
import asyncio

class Socket:
    def __init__(self):
        self.socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )
        self.generel_loop  = asyncio.new_event_loop()

    async def send_data(self,data=None):
        raise NotImplementedError()

    async def listen_socket(self,listen_socket=None):
        raise NotImplementedError()

    async def main(self):
        raise NotImplementedError()

    def start(self):
        self.general_loop.run_until_complete(self.main())

    def set_up(self):
        raise NotImplementedError()