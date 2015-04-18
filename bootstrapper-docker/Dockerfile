# TO_BUILD:     docker build --rm -t coreos-cloud-bootstrapper .

FROM debian:wheezy
MAINTAINER Reza Mohammadi <reza@cafebazaar.ir>
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -q && apt-get upgrade -yq && \
    apt-get install -yq iptables wget syslinux-common supervisor isc-dhcp-server tftpd-hpa

VOLUME ["/data"]

ADD etc-files/coreos-key.txt    /etc/coreos-key.txt

ADD initializer                 /usr/bin/initializer

CMD ["/usr/bin/initializer"]
