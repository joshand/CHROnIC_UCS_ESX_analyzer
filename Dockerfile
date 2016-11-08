FROM chapeter/chronic_docker
MAINTAINER Chad Peterson chapeter@cisco.com

COPY . CHROnIC_UCS_ESX_analyzer/
WORKDIR CHROnIC_UCS_ESX_analyzer
RUN pip install -r requirements

EXPOSE 5000

CMD python populateDB.py && python app.py