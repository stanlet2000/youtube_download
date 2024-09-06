import os
import sys
from gui import main_window
from downloader import YouTubeDownloader
import multiprocessing


if __name__ == "__main__":
    os.environ['PATH'] += os.pathsep + os.path.join(os.path.dirname(__file__), 'ffmpeg', 'bin')
    print(os.environ['PATH'])
    print("!!!")
    multiprocessing.freeze_support()
    ytd = YouTubeDownloader()
    print(ytd.output_path)
    main_window(ytd)
