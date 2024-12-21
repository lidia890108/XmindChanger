import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import filedialog, messagebox

from parser.xmind_parser import parse_xmind
from converter.markdown_converter import convert_xmind_to_markdown as convert_to_markdown
from output.file_writer import write_to_files

class XmindToMarkdownApp:
    def __init__(self, master):
        self.master = master
        master.title("Xmind to Markdown Converter")

        self.label = tk.Label(master, text="选择要转换的 Xmind 文件:")
        self.label.pack()

        self.upload_button = tk.Button(master, text="上传 Xmind 文件", command=self.upload_file)
        self.upload_button.pack()

        self.convert_button = tk.Button(master, text="转换为 Markdown", command=self.convert_file, state="disabled")
        self.convert_button.pack()

        self.file_path = None

    def upload_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Xmind files", "*.xmind")])
        if self.file_path:
            self.label.config(text=f"已选择文件: {self.file_path}")
            self.convert_button.config(state="normal")

    def convert_file(self):
        if self.file_path:
            try:
                sheets_data = parse_xmind(self.file_path)
                markdown_content = convert_to_markdown(sheets_data)
                write_to_files(markdown_content)
                messagebox.showinfo("成功", "转换完成，文件已保存。")
            except Exception as e:
                messagebox.showerror("错误", f"转换过程中发生错误: {e}")

def start_ui():
    root = tk.Tk()
    app = XmindToMarkdownApp(root)
    root.mainloop()