FROM jrottenberg/ffmpeg:4.2-scratch AS ffmpeg

FROM ghcr.io/iqustech/docker-images/python3-base:main

COPY --from=ffmpeg / /

ENV RUNNER_ALLOW_RUNASROOT=0



