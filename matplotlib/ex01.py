import matplotlib.pyplot as plt


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

        hex_color = '#{:02X}{:02X}{:02X}'.format(*rgb_color)
        # 添加文本说明
        rgb_text = f"{hex_color}"
        ax.text(i + 0.5, 0.5, rgb_text, color='black',
                ha='center', va='center', fontsize=8)

    # 保存图形为文件
    plt.savefig(output_file, bbox_inches='tight', pad_inches=0)

    # 显示图形（可选）
    plt.show()


# RGB三元组颜色列表，可以根据需要更改
rgb_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255),
              (255, 255, 0), (255, 165, 0)]

# 生成色块图并保存为PNG文件
output_file = "color_blocks_with_rgb_and_text.png"
generate_color_blocks(rgb_colors, output_file)

print(f"色块图已保存到 {output_file}")
