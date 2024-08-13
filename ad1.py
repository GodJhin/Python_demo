import csv
import pandas as pd
# 读取CSV文件
csv_file_path = 'your_output_file.csv'

# 存储结果的列表
results = []

with open(csv_file_path, 'r') as file:
    # 创建CSV读取器
    csv_reader = csv.reader(file)

    # 逐行读取数据
    for i, row in enumerate(csv_reader, 1):
        # 获取当前行的数值并添加到结果列表
        if len(row) >= 4:
            value = float(row[3])  # 每行的第四列的数值
            results.append(value)

            # 判断是否取够60组数据
            if len(results) >= 60:
                break

            # 每次加9行
            for _ in range(7):
                next(csv_reader, None)
        else:
            print(f"警告：第{i}行数据的列数不足，插入占位值 None")
            results.append(None)

# 打印结果
for i, value in enumerate(results, 1):
    if value is not None:
        print(f"第{i}组数据: {value}")
    else:
        print(f"第{i}组数据: 列数不足，占位值 None")
df = pd.DataFrame({'第一组': results})

df.to_excel('output.xlsx', index=False)
