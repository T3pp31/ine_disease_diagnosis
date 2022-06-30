FROM python:3.9.7
USER root

RUN apt-get update
RUN apt-get -y install locales && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
RUN apt-get -y install python3-pip vim libgl1-mesa-dev libgtk2.0-dev

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN git clone https://github.com/Fu-Te/ine_disease_diagnosis.git
RUN pip install tensorflow -f https://tf.kmtea.eu/whl/stable.html
RUN python -m pip install  flask pillow numpy pandas opencv-python matplotlib scikit-learn seaborn scipy
RUN python -m pip install  keras

EXPOSE 5000