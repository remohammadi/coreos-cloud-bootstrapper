# TO_BUILD:     docker build --rm -t coreos-cloud-bootstrapper .

FROM debian:jessie
MAINTAINER Reza Mohammadi <reza@cafebazaar.ir>
ENV DEBIAN_FRONTEND noninteractive

RUN echo "deb http://ftp.ir.debian.org/debian jessie main" > /etc/apt/sources.list && \
    echo "deb http://ftp.ir.debian.org/debian jessie-updates main" >> /etc/apt/sources.list
RUN apt-get update -q && apt-get upgrade -yq && \
    apt-get install -yq iptables wget syslinux-common pxelinux supervisor isc-dhcp-server tftpd-hpa

RUN apt-get install -yq build-essential python2.7 python2.7-dev python-setuptools && \
    easy_install-2.7 --upgrade pip

VOLUME ["/data"]

ADD etc-files/coreos-key.txt    /etc/coreos-key.txt

ADD initializer                 /usr/bin/initializer

CMD ["/usr/bin/initializer"]
