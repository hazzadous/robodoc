FROM ubuntu:12.04
MAINTAINER Arachnys <techteam@arachnys.com>
RUN apt-get install -qy wget
RUN wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | apt-key add -
RUN echo "deb http://packages.elastic.co/elasticsearch/1.6/debian stable main" | tee -a /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -qy elasticsearch 
