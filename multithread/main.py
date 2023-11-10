import concurrent.futures
import random
import time

# 线程处理函数


def worker(thread_id):
    # 模拟线程的处理过程
    result = f"Thread {thread_id} processed data: {random.randint(1, 100)}"

    # 模拟处理时间
    time.sleep(2)

    return result


# 创建ThreadPoolExecutor线程池
with concurrent.futures.ThreadPoolExecutor() as executor:
    # 提交线程任务
    thread_futures = [executor.submit(worker, i) for i in range(5)]

    # 等待所有线程完成，并获取结果
    results = list(concurrent.futures.as_completed(thread_futures))

# 主线程按照提交的顺序获取处理结果
print("Main thread collecting results:")
for future in thread_futures:
    result = future.result()
    print(result)
