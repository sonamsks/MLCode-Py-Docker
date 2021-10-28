FROM centos

RUN yum install python3 -y
RUN pip3 install pandas
RUN pip3 install numpy
RUN pip3 install sklearn

COPY mlcode.py  /mlcode.py
COPY SalaryData.csv  /SalaryData.csv

ENTRYPOINT [ "python3", "SalaryData.csv" ]
ENTRYPOINT [ "python3", "mlcode.py"]

CMD [ "1.1" ]
