# YouTube Unlisted Video Downloader (GUI via Web Browser)

---

**Fairness Warning: This project contains components optimized using AI generation.**
**User discretion is advised.**

---

A Python-based Tkinter desktop application that automates batch downloading unlisted or public YouTube videos. This containerized build features a self-contained virtual framing engine (`noVNC` & `Xvfb`). It streams the visual application interface directly to your favorite web browser—requiring **zero external X-server apps, configurations, or installations** on your host operating system.

The container automatically handles system fetch pipelines for localized binaries of `yt-dlp` and `ffmpeg`, natively transcoding streams directly into fully compatible MP4 files with functioning AAC audio tracks.

## 🚀 Quick Start (No Setup Required)

Because the container hosts its own internal virtual display desktop stream, you only need to forward a standard network port (`8080`) to interact with the application.

### Run via Linux / macOS / Windows PowerShell

```bash
docker run -d --rm \
  -p 8080:8080 \
  -v ${HOME}/Downloads:/app/downloads \
  mrmoskal/youtube-downloader:latest

```

### 🖥️ How to Access the App

1. Open your web browser (Chrome, Edge, Firefox, etc.).
2. Navigate to: **`http://localhost:8080/vnc.html`**
3. Click the blue **Connect** button.

The application GUI will appear right inside your browser window!

## 💾 Volumes & Persistent Storage

By utilizing the `-v ${HOME}/Downloads:/app/downloads` flag, the application maps its internal target path directly to your host machine's physical `Downloads` folder. All processed MP4 clips will permanently save straight to your machine instead of vanishing when the container finishes running.
