# Use Ubuntu's minimal, hardened LTS release as the base
FROM ubuntu:24.04

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install system utilities, X11 virtual frame buffer, and web streaming tools
RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
    python3.12 \
    python3-pip \
    python3-tk \
    xvfb \
    x11vnc \
    fluxbox \
    novnc \
    websockify \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Symlink python3 to python for application consistency
RUN ln -s /usr/bin/python3 /usr/bin/python

# Set the working directory
WORKDIR /app

# Copy application files (respecting the .dockerignore file)
COPY . /app

# Expose the web browser connection port
EXPOSE 8080

# Create an execution script inside the container to handle the display environment
# FIXED: Replaced /usr/share/novnc/utils/launch.sh with the correct 'novnc_proxy' system binary
RUN echo '#!/bin/bash\n\
Xvfb :1 -screen 0 800x600x24 &\n\
export DISPLAY=:1\n\
sleep 1\n\
fluxbox &\n\
sleep 1\n\
x11vnc -display :1 -nopw -listen localhost -forever &\n\
sleep 1\n\
novnc_proxy --vnc localhost:5900 --listen 8080 &\n\
sleep 1\n\
python main.py\n\
wait' > /app/entrypoint.sh && chmod +x /app/entrypoint.sh

# Launch the virtual desktop pipeline
CMD ["/app/entrypoint.sh"]