import os
os.system('pip install yt_dlp') 
import yt_dlp

# Colored ASCII logo
print("\033[92m TTTTT  \033[93m OOO  \033[94m M   M  \033[91m AAAAA  \033[92m SSSSS \033[0m")
print("\033[92m   T   \033[93m O   O \033[94m MM MM  \033[91m A   A \033[92m S     \033[0m")
print("\033[92m   T   \033[93m O   O \033[94m M M M  \033[91m AAAAA  \033[92m SSS   \033[0m")
print("\033[92m   T   \033[93m O   O \033[94m M   M  \033[91m A   A \033[92m     S \033[0m")
print("\033[92m   T    \033[93m OOO  \033[94m M   M  \033[91m A   A \033[92m SSSSS \033[0m")
print("My Telegram account: @K_DKP")
print("My GITHUB account: @Toma1264git0hub")

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def download_video(url, folder_name):
    ydl_opts = {
        'outtmpl': os.path.join(folder_name, '%(title)s.%(ext)s'),
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Video downloaded successfully\nIn folder: {folder_name}\n(◉‿◉) (◉‿◉)")
    except Exception as e:
        print("An error occurred, try running the tool again.")

folder_name = "/storage/emulated/0/Download/Tomas"  #Download path 
create_folder(folder_name)

video_url = input("Video URL: ")
download_video(video_url, folder_name)
