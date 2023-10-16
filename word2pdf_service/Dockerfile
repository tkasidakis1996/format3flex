FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
	apt-get install -y unoconv libreoffice \
	python3.10 \
	python3.10-dev \
	python3-pip


RUN pip3 install \
	celery

ENV WORD2PDF_SVC_HOME=/home/word2pdf_service

WORKDIR ${WORD2PDF_SVC_HOME}

ENV PYTHONPATH=${WORD2PDF_SVC_HOME}
ENV PYTHONPATH=${WORD2PDF_SVC_HOME}/src:${WORD2PDF_SVC_HOME}