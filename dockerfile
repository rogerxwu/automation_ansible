#CentOS 7 + ansible image V1.0.0
FROM centos:7

LABEL maintainer="xian.wu<xianwuusa@gmail.com>"

# Install base library
RUN yum update -y && yum install -y \
    vim \
    net-tools \
    python3-pip \
    && pip3 install --upgrade pip \
    && pip3 install ansible
     
CMD "/bin/sh"
