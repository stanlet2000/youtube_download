import os
import re
from yt_dlp import YoutubeDL

class YouTubeDownloader:
    def __init__(self, output_path=None):
        """Initialize the downloader with an output directory."""
        if output_path is None:
            # Default to the user's Downloads directory
            output_path = os.path.expanduser('~/Downloads')
        self.output_path = output_path
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

    @staticmethod
    def sanitize_filename(filename):
        """Sanitize the filename to remove invalid characters."""
        return re.sub(r'[\\/*?:"<>|]', "", filename)

    def download_video(self, url, convert_to='mp4'):
        """Download YouTube video and optionally convert it to mp3."""
        ydl_opts = {
            'format': 'bestaudio/best' if convert_to == 'mp3' else 'bestvideo+bestaudio/best',
            'outtmpl': os.path.join(self.output_path, '%(id)s.%(ext)s'),
            'merge_output_format': 'mp4' if convert_to == 'mp4' else None,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }] if convert_to == 'mp3' else [],
        }

        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_id = info_dict.get('id', None)
            video_title = info_dict.get('title', None)
            video_ext = 'mp3' if convert_to == 'mp3' else info_dict.get('ext', None)
            downloaded_file_path = os.path.join(self.output_path, f"{video_id}.{video_ext}")
            sanitized_title = self.sanitize_filename(video_title)
            new_file_path = os.path.join(self.output_path, f"{sanitized_title}.{video_ext}")

            # Rename file if necessary
            if os.path.exists(downloaded_file_path):
                os.rename(downloaded_file_path, new_file_path)
            else:
                print(f"Error: Downloaded file not found at {downloaded_file_path}")
                return f"Error: Downloaded file not found at {downloaded_file_path}"

        print(f"File downloaded and saved as: {new_file_path}")
        return f"File downloaded and saved as: {new_file_path}"

if __name__ == "__main__":
    # Example usage
    downloader = YouTubeDownloader()
    url = 'https://youtu.be/7HgJIAUtICU?si=dTIrJlJoZyU2PTmZ'
    convert_to = 'mp3'  # Change to 'mp4' if needed
    downloader.download_video(url, convert_to=convert_to)
