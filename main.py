import pandas as pd
from tkinter import Tk, filedialog, Label, Button

class ExcelProcessor:
    def __init__(self, master):
        self.master = master
        master.title("Excel处理器")

        self.label = Label(master, text="选择输入CSV文件:")
        self.label.pack()

        self.choose_input_button = Button(master, text="选择文件", command=self.choose_input_file)
        self.choose_input_button.pack()

        self.label = Label(master, text="选择输出CSV文件:")
        self.label.pack()

        self.choose_output_button = Button(master, text="新文件命名", command=self.choose_output_file)
        self.choose_output_button.pack()

        self.process_button = Button(master, text="处理CSV", command=self.process_excel)
        self.process_button.pack()

    def choose_input_file(self):
        self.input_file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])

    def choose_output_file(self):
        self.output_file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])

    def process_excel(self):
        if hasattr(self, 'input_file_path') and hasattr(self, 'output_file_path'):
            remove_blank_rows(self.input_file_path, self.output_file_path)
            print("空白行已删除，新的Excel文件已生成：{}".format(self.output_file_path))
        else:
            print("请选择输入和输出文件。")

def remove_blank_rows(input_file, output_file):
    df = pd.read_excel(input_file)
    df = df.dropna(axis=0, how='all')
    df.to_excel(output_file, index=False)

if __name__ == "__main__":
    root = Tk()
    app = ExcelProcessor(root)
    root.mainloop()
