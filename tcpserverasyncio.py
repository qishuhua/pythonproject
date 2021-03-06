import asyncio


@asyncio.coroutine
def handle_echo(reader, writer):
    data = yield from reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    print('Recviced %r from %r' % (message, addr))
    print('send %r' % message)
    writer.write(data)
    yield from writer.drain()
    print('close client socket')
    writer.close()


loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_echo, '127.0.0.1', 9999, loop=loop)
server = loop.run_until_complete(coro)

print('server on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()

loop.run_until_complete(server.wait_closed())
loop.close()
