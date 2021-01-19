FROM debian:buster

# install core tools
RUN apt -y update
RUN apt install -y curl gnupg

# install jenkins
RUN curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io.key | apt-key add -
RUN echo "deb https://pkg.jenkins.io/debian-stable binary/" > /etc/apt/sources.list.d/jenkins.list
RUN apt -y update && apt -y install jenkins openjdk-11-jdk
ENV JENKINS_HOME=/jenkins

# install docker and dependencies
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN echo "deb https://download.docker.com/linux/debian buster stable" > /etc/apt/sources.list.d/docker.list
RUN apt -y update && apt -y install docker-ce docker-ce-cli containerd.io

# install docker compose
RUN curl -fsSL "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-Linux-x86_64" > /bin/docker-compose
RUN chmod +x /bin/docker-compose

# install bazel
RUN curl -fsSL https://bazel.build/bazel-release.pub.gpg | apt-key add -
RUN echo "deb [arch=amd64] https://storage.googleapis.com/bazel-apt stable jdk1.8" > /etc/apt/sources.list.d/bazel.list
RUN apt -y update && apt -y install bazel

# install llvm-11
RUN curl -fsSL https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add -
RUN echo "deb http://apt.llvm.org/buster/ llvm-toolchain-buster-11 main" > /etc/apt/sources.list.d/llvm-11.list
RUN apt -y update && apt -y install clang-11 libc++-11-dev libc++abi-11-dev

# install OCaml
RUN apt -y install ocaml-nox m4 build-essential
RUN curl -fsSL https://github.com/ocaml/opam/releases/download/2.0.7/opam-2.0.7-x86_64-linux > /bin/opam
RUN chmod +x /bin/opam
RUN opam init --disable-sandboxing -a
RUN opam switch create 4.10.1
RUN eval $(opam env) && opam install -y dune core cmdliner menhir

# install ZeroMQ and other deps
RUN apt -y install -y pkgconf cmake libsodium-dev

RUN mkdir -p /deps

RUN curl -fsSL https://github.com/zeromq/libzmq/releases/download/v4.3.4/zeromq-4.3.4.tar.gz > /deps/zeromq-4.3.4.tar.gz
RUN tar -zxf /deps/zeromq-4.3.4.tar.gz -C /deps
RUN cd /deps/zeromq-4.3.4 && \
  mkdir -p build && \
  cd build && \
  cmake -DCMAKE_BUILD_TYPE=Relase .. && \
  make && \
  make install

RUN curl -fsSL https://github.com/zeromq/cppzmq/archive/v4.7.1.tar.gz > /deps/v4.7.1.tar.gz
RUN tar -zxf /deps/v4.7.1.tar.gz -C /deps
RUN cd /deps/cppzmq-4.7.1 && \
  mkdir -p build && \
  cd build && \
  cmake -DCMAKE_BUILD_TYPE=Relase -DCPPZMQ_BUILD_TESTS=OFF .. && \
  make && \
  make install

# install dependencies
RUN apt -y install libcurl4-openssl-dev libzip-dev

# install pip and python dependencies
RUN apt -y install python3-pip
RUN pip3 install jinja2 click

ENTRYPOINT [ "java", "-jar", "/usr/share/jenkins/jenkins.war" ]
