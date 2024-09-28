#Developer by: @DevPhant0m
#Channel: https://t.me/TEAM_CHICO_CP

import os
import subprocess
import sys

try:
    import yt_dlp
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])
    import yt_dlp

def download_video(url, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    def progress_hook(d):
        if d['status'] == 'downloading':
            print(f"Descargando: {d['_percent_str']} de {d['_total_bytes_str']} a {d['_speed_str']} [ETA: {d['_eta_str']}]")
        elif d['status'] == 'finished':
            print('Descarga completada, guardando el archivo...')

    ydl_opts = {
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',
        'noplaylist': True,
        'quiet': False,
        'progress_hooks': [progress_hook],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    video_url = input("Introduce la URL del video de Facebook: ").strip()
    output_dir = '/storage/emulated/0/Facebook-download/Videos'
    download_video(video_url, output_dir)
    print("Proceso de descarga finalizado.")

if __name__ == "__main__":
    main()