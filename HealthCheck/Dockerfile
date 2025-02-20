FROM redhat/ubi8

RUN yum install python36 -y
RUN pip3 install flask
WORKDIR  /code
EXPOSE 5000
COPY app.py app.py
CMD [ "LWIndia" ]
ENTRYPOINT [ "python3","app.py"]

HEALTHCHECK --interval=10s --retries=4 CMD curl http://127.0.0.1:5001/  || exit 1
