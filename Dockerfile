FROM ubuntu
MAINTAINER Chad Peterson chapeter@cisco.com

RUN apt-get -y install \
  python
  python-pip

RUN pip install --upgrade
RUN pip install -r requirements

COPY . CHROnIC_UCS_ESX_analyzer
WORKDIR CHROnIC_UCS_ESX_analyzer

RUN populateDB.py

EXPOSE 5000

CMD app.py
