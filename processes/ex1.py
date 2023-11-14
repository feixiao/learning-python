import multiprocessing
import time
import logging

# 子进程执行的任务函数


# 配置日志，添加时间戳和进程ID
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - Process:%(process)d - %(message)s')


def task_function(task_id):
    # 这里可以编写具体的任务逻辑
    time.sleep(1)  # 模拟任务执行时间
    result = f"Result for Task {task_id}"
    logging.info(result)
    return result

# 主进程函数，负责派发任务和整理结果


def main():
    num_tasks = 5
    tasks = []

    # 创建进程池
    pool = multiprocessing.Pool()

    # 派发任务给子进程
    for i in range(num_tasks):
        result = pool.apply_async(task_function, args=(i,))
        tasks.append(result)

    # 等待所有子进程任务完成并获取结果
    results = [task.get() for task in tasks]

    # 整理结果按派发顺序输出
    for i, result in enumerate(results):
        logging.info(f"Task {i}: {result}")

    # 关闭进程池
    pool.close()
    pool.join()


if __name__ == "__main__":
    main()
