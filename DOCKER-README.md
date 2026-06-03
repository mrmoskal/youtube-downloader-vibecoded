# YouTube Unlisted Video Downloader (GUI)

---

**Farness Worning: this whole project is _`AI generated`_.**
**user descretion is advised**

---

A Python-based Tkinter desktop application that automates batch downloading unlisted or public YouTube videos. The containerized application automatically syncs the latest backend extraction tools (`yt-dlp`) and multimedia cross-compilers (`ffmpeg`), natively transcoding files directly into fully compatible MP4 assets with working AAC audio streams.

## Quick Start (Running the GUI from Docker)

Because this is a graphical user interface (GUI) application, you must allow the container access to your host machine's display server.

### For Linux Users

Allow local connections to the X server and run the container:

```bash
xhost +local:docker
docker run -it --rm \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v ~/Downloads:/app/downloads \
  YOUR_DOCKERHUB_USERNAME/youtube-downloader:latest

```

### For Windows Users

1. Install an X-Server utility such as **VcXsrv** (XLaunch) or **Xming**.
2. Start the X-Server with **Disable access control** checked.
3. Find your local IPv4 address and run in PowerShell:

```powershell
docker run -it --rm `
  -e DISPLAY=YOUR_IP_ADDRESS:0.0 `
  -v ${HOME}/Downloads:/app/downloads `
  YOUR_DOCKERHUB_USERNAME/youtube-downloader:latest

```

## Volumes & Storage

Make sure to bind your preferred download destination using the `-v` flag (as shown above) so that your downloaded MP4 files are saved directly onto your host computer's hard drive instead of disappearing when the container closes.
