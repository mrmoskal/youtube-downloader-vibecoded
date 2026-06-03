# YouTube Unlisted Video Downloader

---

**Fairness Warning: This project contains components optimized using AI generation.**
**User discretion is advised.**

---

A lightweight, multi-threaded desktop GUI application built with Python and Tkinter for batch downloading YouTube videos. It features automatic asset syncing, tracking updates, and background worker threads to keep the UI highly responsive during large processing queues.

## Key Features

- 🧵 **Multi-Threaded Engine:** Prevents application freezing or window crashing during high-bandwidth operations.
- 📦 **Automatic MP4 Wrapper:** Downloads and converts video structures seamlessly.
- 🔊 **Native AAC Audio Transcoding:** Resolves common Windows Media Player errors by auto-converting non-standard YouTube audio tracks (like Opus/WebM) directly into standard AAC streams.
- 🌐 **Zero-Install Docker GUI:** Runs a headless virtual window environment inside the container, rendering the interface via a local web browser tab (`noVNC`).

---

## 🚀 Docker Hub Deployment

The pre-built, vulnerability-free container image is hosted directly on Docker Hub:
👉 **[Link to Docker Hub Repository](https://hub.docker.com/r/mrmoskal/youtube-downloader)**

### Deploy with One Command

```bash
docker run -d --rm \
  -p 8080:8080 \
  -v ${HOME}/Downloads:/app/downloads \
  mrmoskal/youtube-downloader:latest

```

_Once running, navigate to **`http://localhost:8080/vnc.html`** in any browser and press **Connect**._

---

## 🛠️ Local Development Installation

If you prefer running this application natively on your host system without Docker:

### Prerequisites

- Python 3.11 or higher installed.

### Steps

- Clone the project repository:

```bash
git clone [https://github.com/YOUR_GIT_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_GIT_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME

```

- Run the main Python file:

```bash
python main.py

```

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
