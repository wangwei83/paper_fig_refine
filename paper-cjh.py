import matplotlib.pyplot as plt
import pandas as pd
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签\n
plt.rcParams['font.family'] = 'Times New Roman'  # 设置字体为 Times New Roman
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.rcParams['font.size'] = 9  # 设置字体大小为 9 号
plt.rcParams['axes.titlesize'] = 9  # 设置标题字体大小为 9 号


df_cjh = pd.read_csv('./papers-cjh.csv')
df_cjh_ai = pd.read_csv('./papers-cjh-ai.csv')
df_cjh_chinese = pd.read_csv('./papers-cjh-chinese.csv')

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

fig, ax = plt.subplots(figsize=(10,8))

ax.set_xlabel("Year",fontsize=9)
ax.set_ylabel("Numbers of papers",fontsize=9)

ax.plot(df_cjh.year, df_cjh.num,'b-o',label='Total numbers of papers')
ax.plot(df_cjh_ai.year, df_cjh_ai.num,'r-o',label='Numbers of papers based on AI')
ax.plot(df_cjh_chinese.year, df_cjh_chinese.num,'g-o',label='Numbers of papers from China')

ax.legend(loc='upper left',fontsize=9)



# 设置 x 轴的刻度为整数
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))


plt.axvspan(2004, 2015, facecolor='0.99', alpha=0.5)
plt.axvspan(2015, 2020, facecolor='0.9', alpha=0.5)
plt.axvspan(2020, 2024, facecolor='0.65', alpha=0.5)

ax.axhline(5,linewidth=1,linestyle='-.',color='darkorange')
ax.axvline(2015,linewidth=1,linestyle='-.',color='b')

# ax.axhline(30,linewidth=1,linestyle='-.',color='darkorange')
ax.axvline(2020,linewidth=1,linestyle='-.',color='b')

# ax.annotate("机器学习",
#             xy=(2024, 30), xycoords='data',
#             xytext=(2028, 30), textcoords='data',
#             size=15, va="center", ha="center",
#             arrowprops=dict(facecolor='black', shrink=0.05),
#             )
# ax.annotate("高级计量",
#             xy=(2024, 5), xycoords='data',
#             xytext=(2028, 5), textcoords='data',
#             size=15, va="center", ha="center",
#             arrowprops=dict(facecolor='black', shrink=0.05),
#             )



plt.savefig("paper-cjh-ai-chinese-all-gai20250419-times-size9-all.png", dpi=600, bbox_inches='tight')