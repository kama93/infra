FROM debian:buster

# install base dependencies
RUN apt -y update
RUN apt -y install ssh openssh-server

# this is required for sshd to work
RUN mkdir -p /run/sshd

# install java for the agent
RUN apt -y install openjdk-11-jdk

# install other native build dependencies
RUN apt -y install build-essential cmake curl

# install bazel
RUN curl -fsSL https://bazel.build/bazel-release.pub.gpg | apt-key add -
RUN echo "deb [arch=amd64] https://storage.googleapis.com/bazel-apt stable jdk1.8" > /etc/apt/sources.list.d/bazel.list
RUN apt -y update && apt -y install bazel

# install llvm-11
RUN curl -fsSL https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add -
RUN echo "deb http://apt.llvm.org/buster/ llvm-toolchain-buster-11 main" > /etc/apt/sources.list.d/llvm-11.list
RUN apt -y update && apt -y install clang-11 libc++-11-dev libc++abi-11-dev lld-11

# install OCaml
RUN apt -y install ocaml-nox m4
RUN curl -fsSL https://github.com/ocaml/opam/releases/download/2.0.7/opam-2.0.7-x86_64-linux > /bin/opam
RUN chmod +x /bin/opam

# setup jenkins user
RUN useradd --home /build jenkins && \
    mkdir -p /data && chown jenkins:jenkins /data && \
    mkdir -p /build && chown jenkins:jenkins /build

USER jenkins

# setup ssh keys
RUN mkdir -p /build/.ssh && chmod 500 -R /build/.ssh
COPY authorized_keys /build/.ssh

# initialize ocaml
RUN opam init --disable-sandboxing -a
RUN opam switch create 4.10.1
RUN eval $(opam env) && opam install -y dune core
RUN eval $(opam env) && opam install -y cmdliner menhir re2

# switch back to root
USER root

# install apt tools
RUN apt -y install dpkg-dev dpkg-sig apt-utils

# install third party
RUN apt -y install libssl-dev libcurl4-openssl-dev pkgconf git vim

# install python dependencies
RUN apt -y install python python3-pip python3-dev
RUN python3 -m pip install pytest

# wait for jenkins master connections
ENTRYPOINT [ "/usr/sbin/sshd", "-D" ]
