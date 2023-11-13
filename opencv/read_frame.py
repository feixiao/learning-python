import cv2
import concurrent.futures
import argparse
import logging
import threading
import time


def process_frame(video_path, start_frame, end_frame, output_list, lock):
    cap = cv2.VideoCapture(video_path)

    logging.info(f"Thread {start_frame}: starting")

    thread_output = []  # 用于存储每个线程的输出

    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    for _ in range(start_frame, end_frame):
        # 获取帧。grap 好像不能跳帧 cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
        ret, _ = cap.read()
        if not ret:
            logging.info(f"Thread {start_frame}: failed to retrieve frame")
            break
        # 获取时间戳
        timestamp = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0
        thread_output.append(
            f"{time.ctime()} Thread {start_frame}: Timestamp - {timestamp}")

        # 设置视频流的位置，直接跳过一些帧
        cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_POS_FRAMES) + 20)

        if cap.get(cv2.CAP_PROP_POS_FRAMES) >= end_frame:
            logging.info(f"Thread {start_frame}: reached end frame")
            break

    # 将每个线程的输出添加到共享的列表中
    # 使用锁确保对共享列表的安全访问
    with lock:
        output_list.extend(thread_output)
    cap.release()  # 关闭视频文件
    logging.info(f"Thread {start_frame}: finishing")


def main(video_path, num_threads):
    cap = cv2.VideoCapture(video_path)

    # 获取视频的总帧数
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # 计算每个线程处理的帧范围
    frames_per_thread = total_frames // num_threads
    frame_ranges = [(i * frames_per_thread + 1, min((i + 1) *
                     frames_per_thread, total_frames)) for i in range(num_threads)]

    logging.info(f"Frame ranges: {frame_ranges}")

    # 创建共享的列表，用于存储每个线程的输出
    output_list = []
    # 创建线程锁
    lock = threading.Lock()

    # 使用线程池
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        # 提交帧处理任务给线程池
        futures = [executor.submit(process_frame, video_path, start, end, output_list, lock)
                   for start, end in frame_ranges]

        # 等待所有任务完成
        concurrent.futures.wait(futures)

        logging.info("All threads completed.")
        # logging.info(f"Output list: {output_list.size()}")
        # 打印所有线程的输出
        for output in output_list:
            print(output)

    cap.release()
    cv2.destroyAllWindows()


# python3 read_frame.py /Users/frank/Movies/out.mp4 --num_threads 4
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # 添加命令行参数解析
    parser = argparse.ArgumentParser(
        description='Process video frames and get timestamps.')
    parser.add_argument('video_path', type=str, help='Path to the video file.')
    parser.add_argument('--num_threads', type=int,
                        default=2, help='Number of threads.')

    args = parser.parse_args()

    # 调用主函数
    main(args.video_path, args.num_threads)
