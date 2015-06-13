FROM ubuntu:12.04
MAINTAINER Arachnys <techteam@arachnys.com>
RUN apt-get install -qy python-setuptools
RUN easy_install pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY src/ /
