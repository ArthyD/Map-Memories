FROM python:3.8-alpine
WORKDIR /api
COPY requirement.txt requirement.txt
RUN pip3 install -r requirement.txt
COPY ./main_web.py /api
COPY ./map_project/ /api
CMD ["python3", "main_web.py"]