import csv
import matplotlib.pyplot as plt

# 文件路径列表，根据实际情况修改
csv_files = ['CCD2_20231228 .csv']

# 初始化一个图形
fig, ax = plt.subplots()

# 遍历每个CSV文件
for i, file in enumerate(csv_files):
    dates = []
    height1_values = []
    height2_values = []

    with open(file, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            dates.append(row['日期'])
            height1_values.append(float(row['高度1']))
            height2_values.append(float(row['高度2']))


    # 绘制线图
    ax.plot(dates, height1_values, label=f'高度1 - 文件 {i + 1}')
    ax.plot(dates, height2_values, label=f'高度2 - 文件 {i + 1}')

# 设置坐标轴标签
ax.set_xlabel('日期')
ax.set_ylabel('数据值')

# 显示图例
ax.legend()

# 显示图形
plt.show()
