# Use Ubuntu's minimal, hardened LTS release as the base
FROM ubuntu:24.04

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update, upgrade all system libraries to clear base CVEs, and install requirements
RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
    python3.12 \
    python3-pip \
    python3-tk \
    libx11-6 \
    libxext6 \
    libxrender1 \
    libxtst6 \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Symlink python3 to python for application consistency
RUN ln -s /usr/bin/python3 /usr/bin/python

# Set the working directory
WORKDIR /app

# Copy application files (respecting the .dockerignore file)
COPY . /app

# FIX: If you have an external requirements.txt, this installs dependencies safely.
# If your code relies completely on built-in libraries, this line can safely be removed.
RUN if [ -f requirements.txt ]; then python -m pip install --no-cache-dir --break-system-packages -r requirements.txt; fi

# Run the application
CMD ["python", "main.py"]