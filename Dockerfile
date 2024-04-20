FROM 	ubuntu:latest
WORKDIR /app
COPY 	banda.py .
COPY 	backup.py .
COPY 	ip.py .
RUN 	apt update && apt install cron python2-minimal python2 dh-python python-is-python3 vim pip -y
RUN     pip install requests && pip install speedtest-cli
COPY	cron /opt
RUN     crontab /opt/cron
CMD     [ "cron", "-f" ]