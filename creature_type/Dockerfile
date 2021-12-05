FROM python:3.8
WORKDIR /creature_type
COPY . .
RUN pip3 install -r requirements.txt
RUN python3 create.py
EXPOSE 5000
ENTRYPOINT ["python3","app.py"]