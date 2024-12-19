FROM apache/airflow:2.10.4

USER root

RUN apt update && \
    apt-get install -y openjdk-17-jdk && \
    apt-get install -y ant && \
    apt-get clean;

ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk-amd64

USER airflow

COPY requirements.txt .
RUN pip install -r requirements.txt