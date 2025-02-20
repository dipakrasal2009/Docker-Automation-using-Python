FROM redhat/ubi8

RUN yum install python36 -y
RUN pip3 install flask
WORKDIR  /code
EXPOSE 5000
COPY app.py app.py
CMD [ "LWIndia" ]
ENTRYPOINT [ "python3","app.py"]
