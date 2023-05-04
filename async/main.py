
# python3 协程例子
import asyncio
import time


import asyncio

# 在这个示例中，我们定义了一个协程 hello_world，它打印出 "Hello"，然后等待一秒钟，然后再打印出 "World"。
# 然后我们使用 asyncio.get_event_loop() 获取事件循环对象，然后使用 loop.run_until_complete() 运行协程，直到完成。


async def hello_world():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

loop = asyncio.get_event_loop()
loop.run_until_complete(hello_world())
