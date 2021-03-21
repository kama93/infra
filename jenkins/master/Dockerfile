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

# install pip and python dependencies
RUN apt -y install python3-pip
RUN pip3 install jinja2 click

# install scaleway cli
RUN curl -o /usr/local/bin/scw -L "https://github.com/scaleway/scaleway-cli/releases/download/v2.3.0/scw-2.3.0-linux-x86_64"
RUN chmod +x /usr/local/bin/scw

ENTRYPOINT [ "java", "-jar", "/usr/share/jenkins/jenkins.war" ]
