import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


def choose_file():
    file_path = filedialog.askopenfilename(title="选择文件",
                                           filetypes=[("Excel files", "*.xlsx"), ("CSV files", "*.csv")])
    entry_var.set(file_path)


def generate_scatter_plot():
    file_path = entry_var.get()
    if not file_path:
        status_var.set("请选择文件")
        return

    try:
        # 读取数据
        data = pd.read_excel(file_path) if file_path.endswith('.xlsx') else pd.read_csv(file_path)

        # 生成散点图
        fig, ax = plt.subplots(figsize=(8, 6))
        for column in data.columns:
            ax.scatter(data.index, data[column], label=column)

        ax.set_title("散点图")
        ax.set_xlabel("X轴标签")
        ax.set_ylabel("Y轴标签")
        ax.legend()

        # 创建滚动条
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=3, column=0, columnspan=2, sticky=tk.W + tk.E)

        toolbar = NavigationToolbar2Tk(canvas, window)
        toolbar.update()
        toolbar.grid(row=4, column=0, columnspan=2, sticky=tk.W + tk.E)

        status_var.set("散点图生成成功")

    except Exception as e:
        status_var.set(f"出现错误: {str(e)}")


# 创建主窗口
window = tk.Tk()
window.title("生成散点图工具")

# 文件路径输入框
entry_var = tk.StringVar()
entry = tk.Entry(window, textvariable=entry_var, width=40)
entry.grid(row=0, column=0, padx=10, pady=10)

# 选择文件按钮
select_button = tk.Button(window, text="选择文件", command=choose_file)
select_button.grid(row=0, column=1, padx=10, pady=10)

# 生成散点图按钮
scatter_plot_button = tk.Button(window, text="生成散点图", command=generate_scatter_plot)
scatter_plot_button.grid(row=1, column=0, columnspan=2, pady=10)

# 状态标签
status_var = tk.StringVar()
status_label = tk.Label(window, textvariable=status_var)
status_label.grid(row=2, column=0, columnspan=2, pady=10)

# 运行主循环
window.mainloop()
