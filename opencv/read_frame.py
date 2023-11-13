import cv2
import concurrent.futures
import argparse
import logging


def process_frame(video_path, start_frame, end_frame):
    cap = cv2.VideoCapture(video_path)

    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
    for frame_number in range(start_frame, end_frame):
        # 获取帧
        ret, frame = cap.read()
        if ret is False:
            break

        # 获取时间戳
        timestamp = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0
        print(f"Thread {frame_number}: Timestamp - {timestamp}")
        # 设置视频流的位置，直接跳过一些帧
        cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(
            cv2.CAP_PROP_POS_FRAMES) + 20)

    cap.release()  # 关闭视频文件


def main(video_path, num_threads):
    cap = cv2.VideoCapture(video_path)

    # 获取视频的总帧数
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # 计算每个线程处理的帧范围
    frames_per_thread = total_frames // num_threads
    frame_ranges = [(i * frames_per_thread, min((i + 1) *
                     frames_per_thread, total_frames)) for i in range(num_threads)]

    logging.info(f"Frame ranges: {frame_ranges}")

    # 使用线程池
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        # 提交帧处理任务给线程池
        futures = [executor.submit(process_frame, video_path, start, end)
                   for start, end in frame_ranges]

        # 等待所有任务完成
        concurrent.futures.wait(futures)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # 添加命令行参数解析
    parser = argparse.ArgumentParser(
        description='Process video frames and get timestamps.')
    parser.add_argument('video_path', type=str, help='Path to the video file.')
    parser.add_argument('--num_threads', type=int,
                        default=4, help='Number of threads.')

    args = parser.parse_args()

    # 调用主函数
    main(args.video_path, args.num_threads)
