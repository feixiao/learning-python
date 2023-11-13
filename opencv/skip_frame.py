import cv2
import logging


def main():
    # 设置视频文件路径
    video_path = '/Users/frank/Movies/out.mp4'

    # 打开视频文件
    cap = cv2.VideoCapture(video_path)

    # 检查是否成功打开视频文件
    if not cap.isOpened():
        print("Error: Couldn't open the video file.")
        return

    # 设置跳帧步长
    frame_skip = 100  # 每隔5帧读取一帧

    # 主循环
    while True:
        # 读取一帧
        ret = cap.grab()

        # 检查是否到达视频末尾
        if not ret:
            print("End of video.")
            break

        # 在这里可以对每一帧进行处理，例如显示、保存等

        logging.info(f"Frame {cap.get(cv2.CAP_PROP_POS_FRAMES)}")
        # 跳帧
        for _ in range(frame_skip - 1):
            cap.grab()  # 跳过指定数量的帧
        logging.info(f"After Frame {cap.get(cv2.CAP_PROP_POS_FRAMES)}")

        # 显示当前帧
        # cv2.imshow("Frame", frame)

        # 检查用户是否按下ESC键，如果是则退出循环
        key = cv2.waitKey(30)
        if key == 27:
            break

    # 释放VideoCapture对象
    cap.release()

    # 关闭所有打开的窗口
    cv2.destroyAllWindows()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    main()
