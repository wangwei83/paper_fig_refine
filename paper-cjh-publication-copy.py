import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import textwrap

# 设置全局字体和字体大小
plt.rcParams['font.size'] = 9
plt.rcParams['font.family'] = 'Times New Roman'

# 数据
categories = ['System', 'Computer assisted language learning', 'Frontiers in psychology', 'Innovation in Language Learning and Teaching', 'Computers & education', 'Applied Linguistics']
ca = [1, 2, 3, 4, 5, 6]
values = [9, 4, 4, 3, 3, 3]

# 创建图表
fig, ax = plt.subplots(figsize=(15, 8))

# 绘制柱状图
bars = ax.bar(ca, values, width=0.5, color='skyblue')  # 添加颜色

# 添加标题和标签
ax.set_ylabel('Numbers of papers')  # 使用全局字体设置

# 在每个柱子顶部标注类别名称，使用 textwrap 模块处理文本换行
for bar, category in zip(bars, categories):
    wrapped_text = "\n".join(textwrap.wrap(category, width=12))
    ax.text(bar.get_x() + bar.get_width() / 2, -0.5, wrapped_text, ha='center', va='bottom', fontsize=9, fontdict={'family': 'Times New Roman', 'color': 'black', 'weight': 'bold'})

# 显示图表
plt.savefig("paper-cjh-publication-size-copy.png", dpi=600, bbox_inches='tight')
