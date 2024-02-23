ARG version=8
FROM openjdk:${version}
EXPOSE 9090
RUN apt-get install update && \
    apt-get install mavem -y
RUN maven clean install
ADD . .
ENTRYPOINT [ "java","-jar","/spring-boot-docker.jar" ]
