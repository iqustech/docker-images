FROM    ubuntu:jammy

ENV     TZ=Asia/Tokyo
RUN     ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN     apt-get update && apt-get install -y php-cli php-xml php-zip php-mbstring php-json php-curl php-intl dnsutils iproute2

