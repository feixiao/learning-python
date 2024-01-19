import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from imageio import imread

from skimage.transform import resize
from sklearn.cluster import KMeans
from matplotlib.colors import to_hex, to_rgb


def generate_color_blocks(rgb_colors, output_file):
    num_blocks = len(rgb_colors)

    # 创建一个子图
    fig, ax = plt.subplots()

    # 设置坐标轴范围
    ax.set_xlim(0, num_blocks)
    ax.set_ylim(0, 1)

    # 隐藏坐标轴
    ax.axis('off')

    # 绘制色块和添加文本说明
    for i, rgb_color in enumerate(rgb_colors):
        # 将整数RGB转换为浮点数
        rgb_color_float = (rgb_color[0] / 255.0,
                           rgb_color[1] / 255.0, rgb_color[2] / 255.0)

        ax.fill_between([i, i+1], 0, 1, color=rgb_color_float)

        hex_color = '{}-#{:02X}{:02X}{:02X}'.format(
            i, int(rgb_color[0]), int(rgb_color[1]), int(rgb_color[2]))
        # 添加文本说明
        rgb_text = f"{hex_color}"
        ax.text(i + 0.5, 0.5, rgb_text, color='black',
                ha='center', va='center', fontsize=8)

    # 保存图形为文件
    plt.savefig(output_file, bbox_inches='tight', pad_inches=0)


def get_color_palette(filepath):
    np.random.seed(0)
    img = imread(filepath)

    img = resize(img, (200, 200))
    data = pd.DataFrame(img.reshape(-1, 3),
                        columns=['R', 'G', 'B'])

    kmeans = KMeans(n_clusters=5,
                    random_state=0)
    # Fit and assign clusters
    data['Cluster'] = kmeans.fit_predict(data)

    palette = kmeans.cluster_centers_

    palette_list = list()
    for color in palette:
        palette_list.append([[tuple(color)]])

    colors = []
    for color in palette_list:
        tmp = to_rgb(color[0][0])
        r = int(255 * tmp[0])
        g = int(255 * tmp[1])
        b = int(255 * tmp[2])
        colors.append((r, g, b))

    return colors[0], colors


if __name__ == "__main__":

    filepath = "data/0:1:23.jpg"
    # np.random.seed(0)
    # img = imread(filepath)

    # # Show image
    # plt.axis('off')
    # plt.imshow(img)

    # img = resize(img, (200, 200))
    # data = pd.DataFrame(img.reshape(-1, 3),
    #                     columns=['R', 'G', 'B'])

    # kmeans = KMeans(n_clusters=5,
    #                 random_state=0)

    # # Fit and assign clusters
    # data['Cluster'] = kmeans.fit_predict(data)

    # palette = kmeans.cluster_centers_

    # palette_list = list()
    # for color in palette:
    #     palette_list.append([[tuple(color)]])

    # colors = []
    # for color in palette_list:
    #     color_hex = to_hex(color[0][0])
    #     print(color_hex)
    #     # plt.figure(figsize=(1, 1))
    #     # plt.axis('off')
    #     # plt.imshow(color)
    #     # plt.show()
    #     # print(to_rgb(color[0][0]))
    #     tmp = to_rgb(color[0][0])
    #     colors.append((255 * tmp[0], 255 * tmp[1], 255 * tmp[2]))
    _, colors = get_color_palette(filepath)
    generate_color_blocks(colors, "./data/palette.png")
