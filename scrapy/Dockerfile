FROM jrottenberg/ffmpeg:4.2-scratch AS ffmpeg

FROM python:3.8-slim

COPY --from=ffmpeg / /
COPY requirements.txt /root

RUN apt-get install -y --no-install-recommends tini wget curl fonts-ipafont git  \ 
	python3-setuptools task-spooler \ 
	gcc g++ build-essential cmake jq poppler-utils \
	python3 python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev && \
	pip3 install --upgrade --force-reinstall pip setuptools wheel && \
	pip3 install -r /root/requirements.txt && \
	rm -rf /root/.cache/pip && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
