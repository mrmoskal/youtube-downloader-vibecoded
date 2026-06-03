# YouTube Unlisted Video Downloader

---

**Farness Worning: this whole project is _`AI generated`_.**
**user descretion is advised**

---

A lightweight, multi-threaded desktop GUI application built with Python and Tkinter for batch downloading YouTube videos. It features automatic asset syncing, tracking updates, and background worker threads to keep the UI highly responsive during large processing queues.

## Key Features

- 🧵 **Multi-Threaded Engine:** Prevents application freezing or window crashing during high-bandwidth operations.
- 📦 **Automatic MP4 Wrapper:** Downloads and converts video structures seamlessly.
- 🔊 **Native AAC Audio Transcoding:** Resolves common Windows Media Player errors by auto-converting non-standard YouTube audio tracks (like Opus/WebM) directly into standard AAC streams.
- 🚀 **Zero Setup Dependencies:** On execution, the application automatically handles system fetch pipelines for localized binaries of `yt-dlp` and `ffmpeg`.

---

## 🚀 Docker Hub Deployment

The official pre-built image container can be accessed on Docker Hub here:
👉 **[Link to Docker Hub Repository]** _(Replace this placeholder text with your actual URL once pushed)_

### Run via Docker

```bash
# Allow local display server visibility (Linux)
xhost +local:docker

# Execute Container
docker run -d --rm \
  -p 8080:8080 \
  -v ${HOME}/Downloads:/app/downloads \
  mrmoskal/youtube-downloader:latest

```

---

## 🛠️ Local Development Installation

If you prefer to run this application natively outside of a containerized environment, follow these steps:

### Prerequisites

- Python 3.8 or higher installed on your local operating system.

### Steps

- Clone the project locally:

```bash
git clone [https://github.com/YOUR_GIT_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_GIT_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME

```

- Run the Python file directly:

```bash
python main.py

```

## License

Distributed under the MIT License. See `LICENSE` for more information.
