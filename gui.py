import os
import tkinter as tk
from tkinter import messagebox, filedialog
from downloader import YouTubeDownloader
import multiprocessing

def select_download_path(download_path):
    path = filedialog.askdirectory()
    if path:
        download_path.set(path)

def download_button_click(url_entry, path, ytd):
    url = url_entry.get()
    output_path = os.path.normpath(path.get())
    try:
        ytd.set_download_directory(output_path)
        print(ytd.output_path)
    except ValueError as e:
        print(e)
        print("Path doesn't exist. Want to creat it?(y/n)")
        ans = input()
        if ans == 'y':
            os.makedirs(output_path)
    try:
        result = ytd.download_video(url, convert_to='mp3')
        messagebox.showinfo("Success", result)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def main_window(ytd):
    # 创建 GUI 应用程序的主窗口
    root = tk.Tk()
    root.title("YouTube Downloader")

    # 创建一个存储下载路径的变量
    download_path = tk.StringVar()
    download_path.set(ytd.output_path)  # 默认下载路径为用户的下載

    # 创建并放置标签、输入框和按钮
    tk.Label(root, text="Enter YouTube URL:").pack(pady=10)
    url_entry = tk.Entry(root, width=50)
    url_entry.pack(pady=5)

    tk.Label(root, text="Select Download Path:").pack(pady=10)
    tk.Entry(root, textvariable=download_path, width=50).pack(pady=5)
    tk.Button(root, text="Browse", command=lambda: select_download_path(download_path)).pack(pady=5)

    tk.Button(root, text="Download", command=lambda: download_button_click(url_entry, download_path, ytd)).pack(pady=20)

    # 运行 GUI 主循环
    root.mainloop()

if __name__ == "__main__":
    print("!!!")
    multiprocessing.freeze_support()
    ytd = YouTubeDownloader("./")
    print(ytd.output_path)
    main_window(ytd)
