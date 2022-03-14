# build
FROM python:3.8-slim as build-stage

# deploy
FROM jrottenberg/ffmpeg:4.2-scratch AS ffmpeg

COPY --from=ffmpeg / /
COPY --from=build-stage /root/requirements.txt /root

COPY --from=build-stage /usr/lib/x86_64-linux-gnu/*.so.* /usr/lib/x86_64-linux-gnu/
COPY --from=build-stage /lib/x86_64-linux-gnu/*.so.* /lib/x86_64-linux-gnu/

RUN apt-get update && \
	apt-get install -y --no-install-recommends tini wget curl fonts-ipafont git  && \ 
	python3-setuptools task-spooler && \ 
	gcc g++ build-essential cmake jq poppler-utils && \
	python3 python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev  && \
	pip3 install --upgrade --force-reinstall pip setuptools wheel && \
	pip3 install -r /root/requirements.txt && \
	rm -rf /root/.cache/pip && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
