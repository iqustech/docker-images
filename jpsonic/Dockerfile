FROM openjdk:11-jre-slim

EXPOSE 8080
WORKDIR /workspace
VOLUME ["/var/jpsonic","/data"]



RUN apt-get update && \
    apt-get install -y unzip wget && \
    wget https://github.com/jpsonic/jpsonic/releases/download/v110.1.1/jpsonic-jetty-embedded-for-jdk11-20210929.zip && \
    unzip jpsonic-jetty-embedded-for-jdk11-20210929.zip && \
    rm -rf jpsonic-jetty-embedded-for-jdk11-20210929.zip

EXPOSE 8080
WORKDIR /workspace
VOLUME ["/var/jpsonic","/data"]

ENTRYPOINT ["java","-jar","jpsonic.war"]

