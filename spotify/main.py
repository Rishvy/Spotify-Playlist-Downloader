import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from youtubesearchpython import VideosSearch
import yt_dlp
import sys

# Function to display download progress
def progress_hook(d):
    if d['status'] == 'finished':
        print('\nDownload complete.')
    elif d['status'] == 'downloading':
        progress = d['_percent_str']
        speed = d['_speed_str']
        sys.stdout.write(f'\rDownloading... {progress}, {speed}')
        sys.stdout.flush()

# Authenticate with Spotify API
client_id = '######'
client_secret = '#######'

# Initialize client credentials manager
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

# Initialize Spotify client
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Get user's playlist by its URI
playlist_uri = 'https://open.spotify.com/playlist/######'
playlist = sp.playlist_tracks(playlist_uri)

# Extract song names and artists
songs = [(track['track']['name'], track['track']['artists'][0]['name']) for track in playlist['items']]

# Search for each song on YouTube, print its name, YouTube link, and download the MP3 version
for i, (song_name, artist_name) in enumerate(songs, 1):
    search_query = f"{song_name} {artist_name} official audio"
    videosSearch = VideosSearch(search_query, limit=1)
    result = videosSearch.result()

    if result['result']:
        youtube_link = result['result'][0]['link']

        print(f"\n{i}. {song_name} - {artist_name}")
        print(f"YouTube Link: {youtube_link}")

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'progress_hooks': [progress_hook],
            'ffmpeg_location': '/opt/homebrew/bin/ffmpeg',  # Explicitly set FFmpeg location
             'outtmpl': 'downloads/%(title)s.%(ext)s', #saves t downloads

        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([youtube_link])
        except yt_dlp.utils.DownloadError as e:
            print(f"Error downloading {song_name}: {e}")
    else:
        print(f"No video found for {song_name} - {artist_name}")
