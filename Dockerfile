FROM debian:11.2
RUN apt-get update && apt-get install -y python3.9 python3.9-dev python3-pip
RUN pip install lorem-text
WORKDIR /ToMyApp
COPY . .
CMD ["python3","./main.py", "--lines_number", "4"]