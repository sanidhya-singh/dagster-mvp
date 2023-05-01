# targets latest available Python version
FROM python:slim
LABEL maintainer=sanidhya235@gmail.com

# create directory for Dagster
RUN mkdir -p /opt/app/dagster_mvp

# copy Python environment requirements to container
COPY requirements.txt /opt/app/dagster_mvp

# change working directory
WORKDIR /opt/app/dagster_mvp

# setup and build environment
RUN apt-get update -y && \
 apt-get install sudo -y && \
 sudo apt-get install curl -y && \
 python -m pip install --upgrade pip && \
 python -m pip install setuptools wheel -- upgrade && \
 pip install -r requirements.txt

# change working directory to src folder
WORKDIR /opt/app/dagster_mvp/src

# set DAGSTER_HOME environment variable to the DEV directory
ENV DAGSTER_HOME /opt/app/dagster_mvp/src/dagster_home_dir