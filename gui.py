import os
import tkinter as tk
from tkinter import messagebox
from downloader import download_youtube_video

def download_button_click():
    url = url_entry.get()
    output_path = './downloads'
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    try:
        result = download_youtube_video(url, output_path, convert_to='mp3')
        messagebox.showinfo("Success", result)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# 创建 GUI 应用程序
root = tk.Tk()
root.title("YouTube Downloader")

# 创建并放置标签、输入框和按钮
tk.Label(root, text="Enter YouTube URL:").pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)
download_button = tk.Button(root, text="Download", command=download_button_click)
download_button.pack(pady=20)

# 运行 GUI 主循环
root.mainloop()
