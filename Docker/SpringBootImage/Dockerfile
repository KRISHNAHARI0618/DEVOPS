ARG version=8
FROM openjdk:${version}
EXPOSE 9090
RUN maven clean install
ADD . .
ENTRYPOINT [ "java","-jar","/spring-boot-docker.jar" ]
