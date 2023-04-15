FROM jrottenberg/ffmpeg:4.2-scratch AS ffmpeg

FROM ghcr.io/iqustech/docker-images/python3-base:main

COPY --from=ffmpeg / /

COPY requirements.txt /root

RUN pip3 install -r /root/requirements.txt
