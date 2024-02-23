ARG version=8
FROM openjdk:${version}
EXPOSE 9090
RUN apt-get update && \
    apt-get install maven -y
RUN maven clean install -DskipTests
ADD . .
ENTRYPOINT [ "java","-jar","/spring-boot-docker.jar" ]
