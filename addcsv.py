import os
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import threading

class FileComparerApp:
    def __init__(self, master):
        self.master = master
        master.title("文件对比工具")

        # UI元素
        self.folder_path_var = tk.StringVar()
        self.folder_path_var_2 = tk.StringVar()
        self.output_folder_var = tk.StringVar()
        self.file_entries = []
        self.num_files_var = tk.StringVar()

        tk.Label(master, text="选择第一个文件夹:").grid(row=0, column=0)
        tk.Entry(master, textvariable=self.folder_path_var, state="readonly", width=30).grid(row=0, column=1)
        tk.Button(master, text="选择文件夹", command=self.choose_folder(self.folder_path_var)).grid(row=0, column=2)

        tk.Label(master, text="选择第二个文件夹:").grid(row=1, column=0)
        tk.Entry(master, textvariable=self.folder_path_var_2, state="readonly", width=30).grid(row=1, column=1)
        tk.Button(master, text="选择文件夹", command=self.choose_folder(self.folder_path_var_2)).grid(row=1, column=2)

        tk.Label(master, text="选择要比较的文件数量:").grid(row=2, column=0)
        tk.Entry(master, textvariable=self.num_files_var, width=10).grid(row=2, column=1)
        tk.Button(master, text="确定", command=self.choose_number_of_files).grid(row=2, column=2)

        for i in range(5):  # 最多5个文件
            tk.Label(master, text=f"选择文件{i + 1}:").grid(row=i + 3, column=0)
            file_var = tk.StringVar()
            tk.Entry(master, textvariable=file_var, state="readonly", width=30).grid(row=i + 3, column=1)
            tk.Button(master, text="选择文件", command=lambda var=file_var: self.choose_files(var)).grid(row=i + 3, column=2)
            self.file_entries.append(file_var)

        tk.Label(master, text="选择输出文件夹:").grid(row=8, column=0)
        tk.Entry(master, textvariable=self.output_folder_var, state="readonly", width=30).grid(row=8, column=1)
        tk.Button(master, text="选择文件夹", command=self.choose_folder(self.output_folder_var)).grid(row=8, column=2)

        tk.Button(master, text="开始比较", command=self.start_comparison).grid(row=9, column=0, columnspan=3)

    def choose_folder(self, entry_var):
        def choose_folder_internal():
            folder_path = filedialog.askdirectory()
            entry_var.set(folder_path)

        return choose_folder_internal

    def choose_files(self, entry_var):
        files = filedialog.askopenfilenames(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx;*.xls")])
        entry_var.set(files)

    def choose_number_of_files(self):
        num_files = int(self.num_files_var.get())
        for i in range(num_files):
            file_var = self.file_entries[i]
            self.choose_files(file_var)

    def extract_date_from_filename(self, filename):
        # Extract the date part from the filename (assuming the format CCD4_20231207)
        parts = filename.split("_")
        if len(parts) == 2 and parts[0].startswith("CCD4") and len(parts[1]) == 8:
            return parts[1]
        return None

    def compare_and_save(self, folder_paths, file_path, column_name, output_folder, prefix):
        results = {}

        for folder_path in folder_paths:
            full_path = os.path.join(folder_path, file_path)
            try:
                df = pd.read_csv(full_path)
            except pd.errors.EmptyDataError:
                print(f"Empty CSV file: {full_path}")
                continue
            except pd.errors.ParserError:
                try:
                    df = pd.read_excel(full_path)
                except pd.errors.EmptyDataError:
                    print(f"Empty Excel file: {full_path}")
                    continue
                except pd.errors.ExcelFileError:
                    print(f"Unsupported file format: {full_path}")
                    continue

            outer_diameter_column = df[column_name]
            results[self.extract_date_from_filename(file_path)] = outer_diameter_column

        # Create a DataFrame with the comparison results
        comparison_df = pd.DataFrame(results)

        # Calculate deviation
        deviation = comparison_df.diff(axis=1).dropna(axis=1)
        deviation.columns = [f"{col}_Deviation" for col in deviation.columns]

        # Output file
        output_file_name = f"{prefix}_comparison_result.csv"
        output_file_path = os.path.join(output_folder, output_file_name)
        deviation.to_csv(output_file_path, index=False)

    def start_comparison(self):
        folder_paths = [self.folder_path_var.get(), self.folder_path_var_2.get()]
        output_folder = self.output_folder_var.get()

        for i, file_var in enumerate(self.file_entries):
            file_path = file_var.get()
            if file_path:
                prefix = f"File_{i + 1}"

                # Start a new thread for each file comparison
                thread = threading.Thread(target=self.compare_and_save, args=(folder_paths, file_path, "外径", output_folder, prefix))
                thread.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = FileComparerApp(root)
    root.mainloop()
