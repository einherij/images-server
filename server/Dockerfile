FROM python:3

ADD receiveImages.py /

ENV http_proxy="http://10.168.66.3:8080"
ENV https_proxy="https://10.168.66.3:8080"
RUN python -m pip install --upgrade pip
RUN pip install flask

CMD [ "python", "./receiveImages.py" ]