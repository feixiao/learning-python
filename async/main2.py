import asyncio


# 在这个例子中，我们使用了 asyncio.create_task() 方法来创建两个任务，并在事件循环中并行地运行它们。我们使用 await 来等待它们的完成，这样可以让事件循环在等待这些协程完成时执行其他任务。

async def hello_world():
    print("Hello")
    await asyncio.sleep(1)
    print("World")


async def foo():
    print("Foo")
    await asyncio.sleep(2)
    print("Bar")


async def main():
    task1 = asyncio.create_task(hello_world())
    task2 = asyncio.create_task(foo())
    await task1
    await task2

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
