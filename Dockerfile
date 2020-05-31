FROM centos
WORKDIR /workspace/
RUN yum group install "Development tools" -y
RUN yum install python3 -y \
    python3-devel -y \
    net-tools -y \
    sudo -y \
    openssh-clients -y
RUN pip3 install --upgrade setuptools pip

RUN pip install scikit-learn \
    numpy \
    pandas \
    keras \
    tensorflow

#CMD ["/bin/sh","-c"," python3 $(ls | grep py) "]