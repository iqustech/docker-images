FROM jrottenberg/ffmpeg:4.2-scratch AS ffmpeg

FROM ghcr.io/iqustech/docker-images/python3-base:main

COPY --from=ffmpeg / /

ENV RUNNER_ALLOW_RUNASROOT=0

RUN apt-get update && apt-get install -y --no-install-recommends tini wget curl git \ 
	gcc g++ build-essential cmake jq poppler-utils libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev tk-dev bash && \
	rm -rf /root/.cache/pip && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*