FROM ubuntu
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y ubuntu-desktop
ENV PYTHONUNBUFFERED 1
# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        tzdata \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /code
WORKDIR /code
COPY requirements/base.txt /code/
RUN pip3 install -r base.txt
COPY . /code/
