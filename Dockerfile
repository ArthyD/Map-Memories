FROM debian
RUN apt update && apt install -y python3 python3-pip wpasupplicant
WORKDIR /api
COPY requirement.txt requirement.txt
RUN pip3 install --break-system-packages -r requirement.txt
COPY ./main_web.py /api
COPY ./map_project/ /api/map_project
CMD ["python3", "main_web.py"]