FROM debian:stable-slim

RUN apt-get update && apt-get install -y --no-install-recommends awscli jq && \
	rm -rf /root/.cache/pip && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*