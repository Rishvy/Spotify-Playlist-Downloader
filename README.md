# Spotify Playlist to MP3 Downloader

This project allows you to download the audio of a Spotify playlist as MP3 files by searching for the official audio on YouTube. The tool uses the Spotify API to fetch playlist details and the `yt-dlp` library to download the audio from YouTube.

## Requirements
spotipy
yt-dlp
youtube-search-python

### Python Version
- Python 3.x (Recommended: Python 3.7 or later)

### Dependencies
The following Python packages are required:

- `spotipy`: A Python library for the Spotify Web API.
- `yt-dlp`: A command-line program to download videos from YouTube and other sites.
- `youtube-search-python`: A Python library to search YouTube videos.


Additionally, ffmpeg is required for audio extraction and processing. You can install ffmpeg using Homebrew on macOS:
'brew install ffmpeg'

If you want to change the folder where the MP3 files are saved, modify the 'outtmpl' in the ydl_opts dictionary. For example:
'outtmpl': '/path/to/your/folder/%(title)s.%(ext)s'

