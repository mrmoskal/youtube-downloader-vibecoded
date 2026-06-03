import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading
import os
import subprocess
import urllib.request
import tempfile
import zipfile
import tarfile  # Added to extract Linux ffmpeg builds


class UltimateYoutubeDownloaderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Unlisted Video Downloader")
        self.root.geometry("600x420")
        self.root.resizable(False, False)

        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        title_label = ttk.Label(main_frame, text="YouTube Unlisted Video Downloader", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=(0, 10))

        url_label = ttk.Label(main_frame, text="Paste Links (One URL per line):", font=("Helvetica", 10, "bold"))
        url_label.pack(anchor=tk.W, pady=(5, 2))

        text_frame = ttk.Frame(main_frame)
        text_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))

        self.url_text = tk.Text(text_frame, height=8, width=60, font=("Helvetica", 10))
        scrollbar = ttk.Scrollbar(text_frame, command=self.url_text.yview)
        self.url_text.configure(yscrollcommand=scrollbar.set)

        self.url_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        info_label = ttk.Label(main_frame, text="💡 Retaining original video titles and merging media streams.",
                               font=("Helvetica", 9, "italic"), foreground="green")
        info_label.pack(anchor=tk.W, pady=(0, 15))

        self.download_btn = ttk.Button(main_frame, text="Start Batch Download", command=self.start_download_thread)
        self.download_btn.pack(pady=(0, 10), ipadx=10, ipady=5)

        self.queue_label = ttk.Label(main_frame, text="Queue: 0/0 videos", font=("Helvetica", 10, "bold"))
        self.queue_label.pack(anchor=tk.W)

        self.status_label = ttk.Label(main_frame, text="Status: Ready", font=("Helvetica", 10, "italic"))
        self.status_label.pack(anchor=tk.W, pady=(2, 5))

        self.progress_bar = ttk.Progressbar(main_frame, orient="horizontal", mode="determinate")
        self.progress_bar.pack(fill=tk.X)

    def start_download_thread(self):
        raw_text = self.url_text.get("1.0", tk.END)
        url_list = [line.strip() for line in raw_text.split('\n') if line.strip()]

        if not url_list:
            messagebox.showerror("Error", "Please paste at least one valid YouTube URL.")
            return

        save_dir = filedialog.askdirectory(title="Select Folder to Save Videos")
        if not save_dir:
            return

        self.download_btn.config(state=tk.DISABLED)
        self.progress_bar['value'] = 0

        thread = threading.Thread(target=self.download_batch, args=(url_list, save_dir), daemon=True)
        thread.start()

    def get_latest_tools(self):
        temp_dir = tempfile.gettempdir()
        binary_name = "yt-dlp.exe" if os.name == "nt" else "yt-dlp"
        binary_path = os.path.join(temp_dir, binary_name)

        self.status_label.config(text="Status: Syncing decryption engines...")
        self.root.update_idletasks()

        ytdlp_url = f"https://github.com/yt-dlp/yt-dlp/releases/latest/download/{binary_name}"
        try:
            urllib.request.urlretrieve(ytdlp_url, binary_path)
            if os.name != "nt":
                os.chmod(binary_path, 0o755)
        except Exception as e:
            print(f"Failed to fetch downloader binary: {e}")
            return None, temp_dir

        # FIXED FOR DOCKER: Ensure ffmpeg downloads on Linux too!
        ffmpeg_exe = os.path.join(temp_dir, "ffmpeg.exe" if os.name == "nt" else "ffmpeg")
        ffprobe_exe = os.path.join(temp_dir, "ffprobe.exe" if os.name == "nt" else "ffprobe")

        if not os.path.exists(ffmpeg_exe):
            self.status_label.config(text="Status: Downloading automatic audio/video merger tool...")
            self.root.update_idletasks()

            if os.name == "nt":
                # Windows Download Pipeline
                ffmpeg_url = "https://github.com/yt-dlp/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip"
                zip_path = os.path.join(temp_dir, "ffmpeg.zip")
                try:
                    urllib.request.urlretrieve(ffmpeg_url, zip_path)
                    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                        for file in zip_ref.namelist():
                            if file.endswith("ffmpeg.exe"):
                                with open(ffmpeg_exe, "wb") as f:
                                    f.write(zip_ref.read(file))
                            elif file.endswith("ffprobe.exe"):
                                with open(ffprobe_exe, "wb") as f:
                                    f.write(zip_ref.read(file))
                    os.remove(zip_path)
                except Exception as e:
                    print(f"Automatic Windows ffmpeg integration skipped: {e}")
            else:
                # Linux / Docker Download Pipeline
                ffmpeg_url = "https://github.com/yt-dlp/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-linux64-gpl.tar.xz"
                tar_path = os.path.join(temp_dir, "ffmpeg.tar.xz")
                try:
                    urllib.request.urlretrieve(ffmpeg_url, tar_path)
                    with tarfile.open(tar_path, "r:xz") as tar_ref:
                        for member in tar_ref.getmembers():
                            if member.name.endswith("/ffmpeg"):
                                member.name = os.path.basename(member.name)
                                tar_ref.extract(member, path=temp_dir)
                            elif member.name.endswith("/ffprobe"):
                                member.name = os.path.basename(member.name)
                                tar_ref.extract(member, path=temp_dir)
                    os.chmod(ffmpeg_exe, 0o755)
                    os.chmod(ffprobe_exe, 0o755)
                    os.remove(tar_path)
                except Exception as e:
                    print(f"Automatic Linux ffmpeg integration skipped: {e}")

        return binary_path, temp_dir

    def download_batch(self, url_list, save_dir):
        exe_path, tools_dir = self.get_latest_tools()

        if not exe_path:
            self.status_label.config(text="Status: Tool configuration failed.")
            self.download_btn.config(state=tk.NORMAL)
            messagebox.showerror("Error", "Could not fetch download tools. Check internet connection.")
            return

        total_videos = len(url_list)

        for index, url in enumerate(url_list, start=1):
            self.queue_label.config(text=f"Queue: Downloading {index} of {total_videos}")
            self.status_label.config(text="Status: Processing streams...")
            self.progress_bar['value'] = (index - 1) / total_videos * 100
            self.root.update_idletasks()

            output_template = os.path.join(save_dir, "%(title)s.%(ext)s")

            cmd = [
                exe_path,
                "--rm-cache-dir",
                "--format", "bestvideo+bestaudio/best",
                "--merge-output-format", "mp4",
                "--audio-format", "aac",
                "--ffmpeg-location", tools_dir,
                "--postprocessor-args", "merger:-c:v copy -c:a aac",
                "--output", output_template,
                "--ignore-errors",
                url
            ]

            try:
                self.status_label.config(text="Status: Downloading and merging video tracks...")
                self.root.update_idletasks()
                subprocess.run(cmd, check=True)
            except Exception as e:
                print(f"Failed to download {url}: {e}")

        self.queue_label.config(text=f"Queue: Completed! ({total_videos}/{total_videos})")
        self.status_label.config(text="Status: All files named and saved successfully.")
        self.progress_bar['value'] = 100
        self.download_btn.config(state=tk.NORMAL)

        messagebox.showinfo("Success", f"All {total_videos} videos downloaded, named, and merged successfully!")


if __name__ == "__main__":
    root = tk.Tk()
    app = UltimateYoutubeDownloaderGUI(root)
    root.mainloop()