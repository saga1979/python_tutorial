import asyncio
import time

def test_fun():
    time.sleep(5)
    print('over...')

loop = asyncio.get_event_loop()

loop.call_soon(test_fun )

if not loop.get_debug() :
    loop.set_debug(True)

print(loop.get_debug())
loop.run_forever()



loop.close()
