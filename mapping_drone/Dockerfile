# Base image: Ubuntu 20.04
FROM ubuntu:20.04

# Set non-interactive frontend for APT
ENV DEBIAN_FRONTEND=noninteractive

# Install core dependencies
RUN apt-get update && apt-get install -y \
    build-essential cmake git wget \
    libpcl-dev libvtk7-dev \
    libeigen3-dev libboost-all-dev \
    libflann-dev libgflags-dev \
    python3 python3-pip software-properties-common \
    && apt-get clean

# Step 1: Install CMake (version >= 3.22 for Ceres-Solver)
RUN wget https://github.com/Kitware/CMake/releases/download/v3.22.1/cmake-3.22.1.tar.gz && \
    tar -xzf cmake-3.22.1.tar.gz && \
    cd cmake-3.22.1 && ./bootstrap && make -j$(nproc) && make install && \
    cd .. && rm -rf cmake-3.22.1 cmake-3.22.1.tar.gz

# Step 2: Install Abseil (required for Ceres-Solver)
RUN git clone https://github.com/abseil/abseil-cpp.git /tmp/abseil-cpp && \
    cd /tmp/abseil-cpp && mkdir build && cd build && \
    cmake .. -DCMAKE_POSITION_INDEPENDENT_CODE=ON && \
    make -j$(nproc) && make install && \
    cd / && rm -rf /tmp/abseil-cpp

# Step 3: Install Glog
RUN git clone https://github.com/google/glog.git /tmp/glog && \
    cd /tmp/glog && mkdir build && cd build && \
    cmake .. && make -j$(nproc) && make install && \
    cd / && rm -rf /tmp/glog

# Step 4: Install Ceres-Solver
RUN git clone https://ceres-solver.googlesource.com/ceres-solver /tmp/ceres-solver && \
    cd /tmp/ceres-solver && mkdir build && cd build && \
    cmake .. -DBUILD_TESTING=OFF -DCMAKE_PREFIX_PATH=/usr/local && \
    make -j$(nproc) && make install && \
    cd / && rm -rf /tmp/ceres-solver

# Step 5: Clone and build LOAM
RUN git clone https://github.com/feixyz10/oh_my_loam.git /workspace/oh_my_loam && \
    cd /workspace/oh_my_loam && mkdir build && cd build && \
    cmake .. && make -j$(nproc)

# Set default working directory and command
WORKDIR /workspace/oh_my_loam
CMD ["/bin/bash"]

