FROM python:3.7-alpine
COPY .  /src
WORKDIR /src
RUN pip install -r requirements.txt
EXPOSE  8000
CMD ["output.py"]