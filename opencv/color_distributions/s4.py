
from multiprocessing import Manager, Process

import multiprocessing.pool
import cv2
import numpy as np
from collections import Counter
from PIL import Image
import argparse
import os
import time
import logging


class NoDaemonProcess(multiprocessing.Process):
    # make 'daemon' attribute always return False
    def _get_daemon(self):
        return False

    def _set_daemon(self, value):
        pass
    daemon = property(_get_daemon, _set_daemon)


# We sub-class multiprocessing.pool.Pool instead of multiprocessing.Pool
# because the latter is only a wrapper function, not a proper class.
class NonDaemonPool(multiprocessing.pool.Pool):
    def Process(self, *args, **kwds):
        proc = super(NonDaemonPool, self).Process(*args, **kwds)

        class NonDaemonProcess(proc.__class__):
            """Monkey-patch process to ensure it is never daemonized"""
            @property
            def daemon(self):
                return False

            @daemon.setter
            def daemon(self, val):
                pass

        proc.__class__ = NonDaemonProcess
        return proc


def init_logger():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s.%(msecs)03d %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')


def save_frame_to_file(frame, output_path):
    cv2.imwrite(output_path, frame)
    print(f"Frame saved to {output_path}")


def analyze_frame(frame, output_image_path, most_common_bright_color):
    if most_common_bright_color is not None:
        height, width, _ = frame.shape
        image = Image.new("RGB", (width, height), most_common_bright_color)
        image.save(output_image_path)
        print(f"Most common bright color: {most_common_bright_color}")
        print(f"Image saved to {output_image_path}")
    else:
        print("No bright colors found in the frame.")


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


def init_logger():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s.%(msecs)03d %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

# Define your functions (save_frame_to_file, analyze_frame, is_bright_color, get_most_common_bright_color, FrameProcessor) here...


def analyze_frames(video_path, frame_ranges, skip_frames, dump_frames, dump_images):

    # 创建进程池
    pool = NonDaemonPool()
    tasks = []
    for frame_range in frame_ranges:
        # logging.info(f"Processing frame range: {frame_range}")
        result = pool.apply_async(process_frame_range, args=(
            video_path, frame_range, skip_frames, dump_frames, dump_images))
        tasks.append(result)

    # results = Manager,
    # 等待所有子进程任务完成并获取结果

    results = [task.get() for task in tasks]
    pool.close()
    pool.join()

    sorted_results = sorted(results.items(), key=lambda x: x[0])
    for timestamp, color in sorted_results:
        logging.info(
            f"Timestamp: {timestamp}, Most common bright color: {color}"
        )


def process_frame_range(video_path, frame_range, skip_frames, dump_frames, dump_images):
    init_logger()
    cap = cv2.VideoCapture(video_path)
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_range[0])

    lock = Manager().Lock()
    results = []
    for frame_position in range(frame_range[0], frame_range[1] + 1, skip_frames):
        timestamp = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0

        ret, frame = cap.read()

        if not ret:
            logging.error(
                f"Error reading frame at position {frame_position}, {timestamp}"
            )
            return results

        most_common_bright_color = get_most_common_bright_color(frame)

        if most_common_bright_color is not None:
            with lock:
                results[timestamp] = most_common_bright_color
                logging.info(
                    f"Processed frame at position {frame_position}"
                )

                if dump_frames:
                    frame_filename = f"frame_{frame_position}.png"
                    frame_path = os.path.join("frames", frame_filename)
                    save_frame_to_file(frame, frame_path)
                    print(f"Frame saved to {frame_path}")

                if dump_images:
                    image_filename = f"color_image_{frame_position}.png"
                    image_path = os.path.join(
                        "color_images", image_filename)
                    analyze_frame(frame, image_path,
                                  most_common_bright_color)
        return results


# python3 s4.py /Users/frank/Movies/test_file/视频脚本/超级马力大电影_来到猩猩.mp4 --frame_ranges 0-10 --skip_frames 1
# python3 s4.py /Users/frank/Movies/test_file/视频脚本/超级马力大电影_来到猩猩.mp4 --frame_ranges 0-5 6-10 --skip_frames 1
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Process video frames and analyze RGB values using multiple processes.")
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
    # multiprocessing.set_start_method('spawn')

    start_time = time.time()
    frame_ranges = [list(map(int, fr.split('-'))) for fr in args.frame_ranges]

    if args.dump_frames:
        os.makedirs("frames", exist_ok=True)
    if args.dump_images:
        os.makedirs("color_images", exist_ok=True)

    analyze_frames(args.video_path, frame_ranges,
                   args.skip_frames, args.dump_frames, args.dump_images)

    end_time = time.time()
    elapsed_time = end_time - start_time

    logging.info(f"Total running time: {elapsed_time:.2f} seconds")
