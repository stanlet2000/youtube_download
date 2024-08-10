import os
import sys
from moviepy.editor import VideoFileClip, AudioFileClip
from yt_dlp import YoutubeDL
import re

def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "", filename)

def download_youtube_video(url, output_path, convert_to='mp4'):
    # 下载视频
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(id)s.%(ext)s'),
        'merge_output_format': 'mp4',
    }
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_id = info_dict.get('id', None)
        video_title = info_dict.get('title', None)
        video_ext = info_dict.get('ext', None)
        downloaded_file_path = os.path.join(output_path, f"{video_id}.{video_ext}")
        sanitized_title = sanitize_filename(video_title)
        new_file_path = os.path.join(output_path, f"{sanitized_title}.{video_ext}")
        os.rename(downloaded_file_path, new_file_path)


    print(f"Downloaded file path: {new_file_path}")

    if not os.path.exists(new_file_path):
        print(f"Error: Downloaded file not found at {new_file_path}")
        return  # Exit the function if the file is not found

    if convert_to == 'mp3':
        try:
            # 转换为 mp3
            video_clip = VideoFileClip(new_file_path)
            audio_clip = video_clip.audio
            audio_clip.write_audiofile(os.path.join(output_path, f"{sanitized_title}.mp3"))
            audio_clip.close()
            video_clip.close()
            # 可选地，删除原始 mp4 文件
            os.remove(new_file_path)
        except Exception as e:
            print(e)
            return e

    print(f"File downloaded and converted to {convert_to} at {output_path}")
    return f"File downloaded and converted to {convert_to} at {output_path}"

if __name__ == "__main__":
    # Example usage
    download_youtube_video('https://youtu.be/7HgJIAUtICU?si=dTIrJlJoZyU2PTmZ', './', convert_to='mp3')
