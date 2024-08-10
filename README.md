# YouTube Video Downloader with GUI

This project provides a simple graphical user interface (GUI) to download YouTube videos and convert them to MP3 formats. The application uses `yt-dlp` for downloading and `MoviePy` for video/audio processing.

## Features

- Download YouTube videos by providing a URL.
- Convert downloaded videos to MP3 formats.
- Simple and intuitive GUI.

## Prerequisites

- Python 3.x
- `yt-dlp`
- `moviepy`
- `tkinter`
- `ffmpeg` 

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Download `ffmpeg`:**

    - [Download FFmpeg](https://ffmpeg.org/download.html)
  
    Place the `ffmpeg` binary inside the `ffmpeg` directory in the project.

## Usage

1. **Run the application:**

    ```bash
    python main.py
    ```

2. **Using the GUI:**

    - Enter the YouTube URL.
    - Choose the output directory.
    - Click "Download" to start the download and conversion process.

## Packaging

To create a standalone executable that includes `ffmpeg`, follow these steps:

1. **Install PyInstaller:**

    ```bash
    pip install pyinstaller
    ```

2. **Create a spec file and modify it:**

    ```bash
    pyinstaller main.py
    ```

    - Modify the generated `.spec` file to include the `ffmpeg` binary.

3. **Build the executable:**

    ```bash
    pyinstaller main.spec
    ```

4. **Find the executable in the `dist` folder:**

    - The final executable will be located in the `dist` directory.

## Attribution

- Icons used in the GUI are from Flaticon. You can find them [here](https://www.flaticon.com/free-icons/play-button).
  - <a href="https://www.flaticon.com/free-icons/play-button" title="play button icons">Play button icons created by bqlqn - Flaticon</a>
- Project was developed with assistance from [ChatGPT](https://chatgpt.com/share/40d65036-7110-4cfd-b84a-53071eaa5406).

## Contributing

Feel free to submit issues or pull requests if you have any suggestions or improvements.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
