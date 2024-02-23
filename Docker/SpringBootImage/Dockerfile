ARG version=8
FROM openjdk:${version}
EXPOSE 9090
WORKDIR /app
RUN apt-get update && \
    apt-get install-y maven
RUN maven clean install
ADD . .
ENTRYPOINT [ "java","-jar","/spring-boot-docker.jar" ]
