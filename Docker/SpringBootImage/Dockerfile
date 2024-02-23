ARG version=11
FROM openjdk:${version}
EXPOSE 9090
WORKDIR /app
RUN apt-get update && \
    apt-get install -y maven
ADD . .
RUN maven clean install

ENTRYPOINT [ "java","-jar","/spring-boot-docker.jar" ]
