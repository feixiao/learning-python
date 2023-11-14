import cv2
import numpy as np
from collections import Counter
from PIL import Image
import argparse


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


def save_frame_to_file(frame, output_path):
    cv2.imwrite(output_path, frame)
    print(f"Frame saved to {output_path}")


def analyze_frame(frame, output_image_path):
    most_common_bright_color = get_most_common_bright_color(frame)

    if most_common_bright_color is not None:
        height, width, _ = frame.shape
        image = Image.new("RGB", (width, height), most_common_bright_color)
        image.save(output_image_path)
        print(f"Most common bright color: {most_common_bright_color}")
        print(f"Image saved to {output_image_path}")
    else:
        print("No bright colors found in the frame.")


def process_video(video_path, frame_number, output_frame_path, output_image_path):
    cap = cv2.VideoCapture(video_path)
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number - 1)
    ret, frame = cap.read()

    if not ret:
        print("Error reading frame.")
        return

    save_frame_to_file(frame, output_frame_path)
    analyze_frame(frame, output_image_path)
    cap.release()


def main():
    parser = argparse.ArgumentParser(
        description="Process video frames and analyze RGB values.")
    parser.add_argument("video_path", type=str, help="Path to the video file.")
    parser.add_argument("frame_number", type=int,
                        help="Frame number to analyze.")
    parser.add_argument("output_frame_path", type=str,
                        help="Path to save the output frame.")
    parser.add_argument("output_image_path", type=str,
                        help="Path to save the output image.")

    args = parser.parse_args()

    process_video(args.video_path, args.frame_number,
                  args.output_frame_path, args.output_image_path)


# python3 s1.py /Users/frank/Movies/test_file/视频脚本/超级马力大电影_来到猩猩.mp4 100 /Users/frank/workspace/github/python/learning-python/opencv/color_distributions/img/output_frame.png /Users/frank/workspace/github/python/learning-python/opencv/color_distributions/img/output_image.png
# python3 s1.py /Users/frank/Movies/test_file/视频脚本/超级马力大电影_来到猩猩.mp4 300 /Users/frank/workspace/github/python/learning-python/opencv/color_distributions/img/output_frame.png /Users/frank/workspace/github/python/learning-python/opencv/color_distributions/img/output_image.png
if __name__ == "__main__":
    main()
