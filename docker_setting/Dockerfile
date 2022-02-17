FROM python:3.9.7
USER root

RUN apt-get update
RUN apt-get -y install locales && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN apt install -y libopencv-dev opencv-data
RUN git clone https://github.com/Fu-Te/ine_disease_diagnosis.git
RUN pip install flask tensorflow keras numpy pillow opencv-python pandas

EXPOSE 5000