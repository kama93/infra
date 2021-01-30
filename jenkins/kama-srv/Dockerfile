FROM debian:buster

ARG apt_password

# base dependencies for jenkins
RUN apt -y update 
RUN apt -y install ssh openssh-server

# this is required for sshd to work
RUN mkdir -p /run/sshd

# install java for the agent
RUN apt -y install openjdk-11-jdk

# install common dependencies
RUN apt -y install curl gnupg

# install local apt repository
RUN apt -y install ca-certificates
RUN echo "deb [trusted=yes] https://apt.kamilaburzynska.com /" >> /etc/apt/sources.list.d/kamilaburzynska.list
RUN echo "machine apt.kamilaburzynska.com" >> /etc/apt/auth.conf.d/kamilaburzynska.conf && \
    echo "login apt" >> /etc/apt/auth.conf.d/kamilaburzynska.conf && \
    echo "password ${apt_password}" >> /etc/apt/auth.conf.d/kamilaburzynska.conf
RUN apt -y update

# install libc++
RUN curl -fsSL https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add -
RUN echo "deb http://apt.llvm.org/buster/ llvm-toolchain-buster-11 main" > /etc/apt/sources.list.d/llvm-11.list
RUN apt -y update && apt -y install libc++-11-dev libc++abi-11-dev

# setup jenkins user
RUN useradd --home /build jenkins && \
    mkdir -p /data && chown jenkins:jenkins /data && \
    mkdir -p /build && chown jenkins:jenkins /build

USER jenkins

# setup ssh keys
RUN mkdir -p /build/.ssh && chmod 500 -R /build/.ssh
COPY authorized_keys /build/.ssh

USER root

# setup sudo
RUN apt -y install sudo
RUN usermod -aG sudo jenkins
RUN echo "jenkins ALL=(ALL) NOPASSWD: /usr/bin/apt" >> /etc/sudoers.d/jenkins

# install aws dependencies for accessing S3
RUN apt -y install python3 python3-pip
RUN python3 -m pip install awscli awscli-plugin-endpoint
RUN mkdir -p /build/.aws
COPY aws_config /build/.aws/config

# wait for jenkins master connections
ENTRYPOINT [ "/usr/sbin/sshd", "-D" ]
