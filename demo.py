import pandas as pd
import tkinter as tk
from tkinter import filedialog


def remove_blank_rows(input_file, output_file):
    data = pd.read_excel(input_file) if input_file.endswith('.xlsx') else pd.read_csv(input_file)
    data = data.dropna(how='all')
    data.to_excel(output_file, index=False) if output_file.endswith('.xlsx') else data.to_csv(output_file, index=False)


def select_file():
    file_path = filedialog.askopenfilename(title="选择文件",
                                           filetypes=[("Excel files", "*.xlsx"), ("CSV files", "*.csv")])
    entry_var.set(file_path)



def process_file():
    input_file = entry_var.get()
    if not input_file:
        status_var.set("请选择文件")
        return

    output_file = input_file.replace('.xlsx', '_processed.xlsx').replace('.csv', '_processed.csv')

    remove_blank_rows(input_file, output_file)

    status_var.set(f"处理完成，文件保存为: {output_file}")


# 创建主窗口
root = tk.Tk()
root.title("文件处理工具")

# 文件路径输入框
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, width=40)
entry.grid(row=0, column=0, padx=10, pady=10)

# 选择文件按钮
select_button = tk.Button(root, text="选择文件", command=select_file)
select_button.grid(row=0, column=1, padx=10, pady=10)

# 处理文件按钮
process_button = tk.Button(root, text="处理文件", command=process_file)
process_button.grid(row=1, column=0, columnspan=2, pady=10)

# 状态标签
status_var = tk.StringVar()
status_label = tk.Label(root, textvariable=status_var)
status_label.grid(row=2, column=0, columnspan=2, pady=10)

# 运行主循环
root.mainloop()
