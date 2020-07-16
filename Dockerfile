FROM python:3.8

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

ADD src app/src
WORKDIR app
ADD requirements.txt .
ADD run_locally.sh .

CMD ["./run_locally.sh"]