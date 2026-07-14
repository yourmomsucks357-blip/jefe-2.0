# Use a CUDA-enabled base image for GPU support
FROM nvidia/cuda:12.1.0-base-ubuntu22.04

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    python3 \
    python3-pip \
    zstd \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Install Open-WebUI and Python dependencies
RUN pip install open-webui PyPDF2 cryptography requests python-whois

# Set environment variables for Ollama
ENV OLLAMA_HOST=0.0.0.0
ENV OLLAMA_MODELS=/data/ollama/models

# Copy toolkit scripts
COPY scripts/ /app/scripts/
WORKDIR /app

# Start Ollama and Open-WebUI
ENTRYPOINT ["sh", "-c", "ollama serve & sleep 10 && ollama pull dolphin-llama3:70b && open-webui serve --port 7860"]
