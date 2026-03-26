FROM debian:bookworm-slim

# System dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-venv \
    python3-dev \
    git \
    git-lfs \
    curl \
    wget \
    ssh \
    build-essential \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.cargo/bin:/root/.local/bin:$PATH"

# Python tooling
RUN uv tool install black && \
    uv tool install ruff && \
    uv tool install pytest && \
    uv tool install ipython

# Git LFS
RUN git lfs install

# Workspace
WORKDIR /workspace

CMD ["/bin/bash"]