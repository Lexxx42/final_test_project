# base image
FROM ubuntu
ARG DEBIAN_FRONTEND=noninteractive

ENV CHROME_VERSION "111.0.5563.146-1"
ENV FIREFOX_VERSION "111.0.1"

# installing of work directory (by default) in image
WORKDIR /autotests

# installing of requirements
RUN set -eux; \
	apt-get update; \
	apt-get install -y --no-install-recommends \
        software-properties-common \
        gnupg \
        ca-certificates \
	; \
    add-apt-repository --yes ppa:deadsnakes/ppa; \
    apt-get install -y --no-install-recommends \
        python3.11 \
        python3-pip \
        wget \
        curl \
        unzip \
        bzip2 \
    ; \
    apt-get purge -y firefox; \
    apt-get install -y --no-install-recommends \
        firefox-esr; \
    curl -L https://github.com/mozilla/geckodriver/releases/download/v0.32.2/geckodriver-v0.32.2-linux64.tar.gz | tar xz -C /usr/local/bin; \
    wget --no-check-certificate https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_${CHROME_VERSION}_amd64.deb; \
    apt-get install -qqyf ./google-chrome-stable_${CHROME_VERSION}_amd64.deb; \
    rm google-chrome-stable_${CHROME_VERSION}_amd64.deb; \
    wget https://chromedriver.storage.googleapis.com/111.0.5563.64/chromedriver_linux64.zip; \
    unzip chromedriver_linux64.zip; \
    mv /usr/bin/google-chrome-stable /usr/bin/google-chrome; \
	rm -rf /var/lib/apt/lists/*

# copying project to image
COPY . .

# installing requirements from pip
RUN pip3 install -r requirements.txt