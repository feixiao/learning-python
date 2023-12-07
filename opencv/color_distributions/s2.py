import cv2
import numpy as np
from collections import Counter
from PIL import Image
import argparse
import threading
import os
import time
import logging

logging.basicConfig(level=logging.INFO,
                    # filename='new.log',
                    # filemode='w',
                    format='%(asctime)s.%(msecs)03d %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def save_frame_to_file(frame, output_path):
    cv2.imwrite(output_path, frame)
    logging.info(f"Frame saved to {output_path}")


def analyze_frame(frame, output_image_path, most_common_bright_color):
    if most_common_bright_color is not None:
        height, width, _ = frame.shape
        image = Image.new("RGB", (width, height), most_common_bright_color)
        image.save(output_image_path)
        logging.info(f"Most common bright color: {most_common_bright_color}")
        logging.info(f"Image saved to {output_image_path}")
    else:
        logging.info("No bright colors found in the frame.")


def is_bright_color(color):
    # 判断颜色是否亮，适合灯光显示的逻辑
    # 根据实际情况调整亮度阈值和颜色通道的权重
    brightness_threshold = 50
    weighted_brightness = 0.299 * color[0] + \
        0.587 * color[1] + 0.114 * color[2]
    return weighted_brightness > brightness_threshold


def get_most_common_bright_color(frame):
    pixels = frame.reshape((-1, 3))
    counter = Counter(map(tuple, pixels))

    # 过滤掉较暗的颜色
    bright_colors = [color for color in counter if is_bright_color(color)]

    if not bright_colors:
        return None

    # 找到出现次数最多的亮色
    most_common_bright_color = max(bright_colors, key=counter.get)
    return most_common_bright_color


class FrameProcessor(threading.Thread):
    def __init__(self, cap, frame_range, skip_frames, results, lock, dump_frames, dump_images):
        super(FrameProcessor, self).__init__()
        self.cap = cap
        self.frame_range = frame_range
        self.skip_frames = skip_frames
        self.results = results
        self.lock = lock
        self.dump_frames = dump_frames
        self.dump_images = dump_images

    def run(self):
        # 读取帧区间内的所有帧，根据 skip_frames 跳帧
        for frame_position in range(self.frame_range[0], self.frame_range[1] + 1, self.skip_frames):
            # 设置要获取的帧的位置
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame_position)
            # 获取帧的时间戳
            timestamp = self.cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0

            # 读取帧
            ret, frame = self.cap.read()

            if not ret:
                logging.error(
                    f"Error reading frame at position {frame_position}, {timestamp}")
                return

            logging.info(
                f"{self.getName()} Processing frame at position {frame_position} get_most_common_bright_color")
            # 获取最常见的亮色
            most_common_bright_color = get_most_common_bright_color(frame)

            logging.info(
                f"{self.getName()} Processing frame at position {frame_position} get_most_common_bright_color done")

            if most_common_bright_color is not None:
                with self.lock:
                    self.results[timestamp] = most_common_bright_color
                    logging.info(
                        f"{self.getName()} Processed frame at position {frame_position}")

                    # 保存数据帧
                    if self.dump_frames:
                        frame_filename = f"frame_{frame_position}.png"
                        frame_path = os.path.join("frames", frame_filename)
                        save_frame_to_file(frame, frame_path)
                        print(f"Frame saved to {frame_path}")

                    # 保存颜色图片
                    if self.dump_images:
                        image_filename = f"color_image_{frame_position}.png"
                        image_path = os.path.join(
                            "color_images", image_filename)
                        analyze_frame(frame, image_path,
                                      most_common_bright_color)

# 其他函数保持不变...


def analyze_frames(video_path, frame_ranges, skip_frames, dump_frames, dump_images):
    cap = cv2.VideoCapture(video_path)

    # 初始化线程锁
    lock = threading.Lock()

    # 存储处理结果
    results = {}

    threads = []
    for frame_range in frame_ranges:
        # 每个线程打开新的视频文件
        cap_thread = cv2.VideoCapture(video_path)

        # 创建并启动线程进行处理
        thread = FrameProcessor(
            cap_thread, frame_range, skip_frames, results, lock, dump_frames, dump_images)
        thread.start()
        threads.append((thread, cap_thread))

    # 等待所有线程完成
    for thread, cap_thread in threads:
        thread.join()

    # 释放每个线程的视频流
    cap_thread.release()

    # 按照帧位置排序结果
    sorted_results = sorted(results.items(), key=lambda x: x[0])

    # 打印结果
    for timestamp, color in sorted_results:
        logging.info(
            f"Timestamp: {timestamp}, Most common bright color: {color}")


# python3 s2.py /Users/frank/Movies/test_file/视频脚本/超级马力大电影_来到猩猩.mp4 --frame_ranges 0-100 200-300 --dump_frames --dump_images
# python3 s2.py /Users/frank/Movies/test_file/视频脚本/超级马力大电影_来到猩猩.mp4 --frame_ranges 0-10 --skip_frames 1
# python3 s2.py /Users/frank/Movies/test_file/视频脚本/超级马力大电影_来到猩猩.mp4 --frame_ranges 0-5 6-10 --skip_frames 1
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Process video frames and analyze RGB values using multiple threads.")
    parser.add_argument("video_path", type=str, help="Path to the video file.")
    parser.add_argument("--dump_frames", action="store_true",
                        help="Dump data frames to files.")
    parser.add_argument("--dump_images", action="store_true",
                        help="Dump color images to files.")
    parser.add_argument("--frame_ranges", nargs='+', type=str,
                        help="Frame ranges to process, each in the format 'start-end'.")
    parser.add_argument("--skip_frames", type=int, default=30,
                        help="Number of frames to skip between processed frames.")

    args = parser.parse_args()

    start_time = time.time()  # 记录开始时间
    # 解析帧区间
    frame_ranges = [list(map(int, fr.split('-'))) for fr in args.frame_ranges]

    # 创建保存帧和颜色图片的目录
    if args.dump_frames:
        os.makedirs("frames", exist_ok=True)
    if args.dump_images:
        os.makedirs("color_images", exist_ok=True)

    analyze_frames(args.video_path, frame_ranges,
                   args.skip_frames, args.dump_frames, args.dump_images)

    end_time = time.time()  # 记录结束时间
    elapsed_time = end_time - start_time  # 计算总运行时间

    logging.info(f"Total running time: {elapsed_time:.2f} seconds")
