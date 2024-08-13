import csv
from datetime import datetime

# 读取CSV文件
with open("CCD0_20231228 .csv", "r") as f:
    reader = csv.reader(f)
    rows = [list(map(str.strip, row)) for row in reader]

# 获取标题行的索引
header = rows[0]
date_index = header.index("日期")

# 新建一个CSV文件来存储满足条件的行
with open("output2.csv", "w", newline='') as output_file:
    writer = csv.writer(output_file)

    # 写入新文件的标题行
    writer.writerow(header)

    # 从第三行开始循环计算时间差
    for i in range(18, len(rows), 17):
        # 检查当前行和前一行是否有足够的列数
        if len(rows[i]) > date_index and len(rows[i-17]) > date_index:
            current_time_str = rows[i][date_index]
            previous_time_str = rows[i-17][date_index]

            # 将时间字符串转换为datetime对象
            current_time = datetime.strptime(current_time_str, "%H:%M:%S")
            previous_time = datetime.strptime(previous_time_str, "%H:%M:%S")

            # 计算时间差
            time_difference = current_time - previous_time

            # 打印信息，以便调试
            print(f"行 {i-17} 时间：{previous_time_str}, 行 {i} 时间：{current_time_str}, 时间差：{time_difference.total_seconds()} 秒")

            # 如果时间差大于40秒，则写入新文件
            if time_difference.total_seconds() > 40:
                writer.writerow(rows[i-17])
                writer.writerow(rows[i])
        else:
            print(f"行 {i} 或 行 {i-17} 列数不足，无法处理。")
