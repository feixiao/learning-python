import threading


# 下面是一个简单的Python程序，它使用多线程来分析和处理文本文件。程序将文本文件分成N段，每段由一个线程处理，线程会查找指定的关键字并返回关键字所在的行数。
# 最后，主线程将所有线程的结果合并。

# 这个函数接受一个文本段落和一个关键字作为参数，然后在段落中查找关键字，返回包含关键字的行号列表。
def process_segment(segment, keyword):
    result = []
    lines = segment.split('\n')
    for i, line in enumerate(lines, start=1):
        if keyword in line:
            result.append(i)
    return result

# 这个函数接受文件名、线程数量和关键字作为参数。首先，它读取文件内容，然后将文件内容分成N段，其中N是线程数量。接下来，它创建一个线程池，每个线程处理一个文本段，并调用process_segment函数来查找关键字。最后，主线程等待所有线程完成，并将结果合并后返回。


def analyze_file(filename, num_threads, keyword):
    with open(filename, 'r') as file:
        content = file.read()

    segment_size = len(content) // num_threads
    segments = [content[i:i+segment_size]
                for i in range(0, len(content), segment_size)]

    threads = []
    results = []

    def worker(segment):
        result = process_segment(segment, keyword)
        results.extend(result)

    for segment in segments:
        thread = threading.Thread(target=worker, args=(segment,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # 对结果进行排序
    results.sort()
    return results


if __name__ == "__main__":
    filename = input("请输入文件名：")
    num_threads = int(input("请输入线程数："))
    keyword = input("请输入要查找的关键字：")

    results = analyze_file(filename, num_threads, keyword)

    print(f"关键字'{keyword}'出现在以下行数：")
    print(results)
