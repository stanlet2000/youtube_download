import os
import sys
from gui import main
import multiprocessing


if __name__ == "__main__":
    os.environ['PATH'] += os.pathsep + os.path.join(os.path.dirname(__file__), 'ffmpeg', 'bin')
    print(os.environ['PATH'])
    print("!!!")
    multiprocessing.freeze_support()
    main()