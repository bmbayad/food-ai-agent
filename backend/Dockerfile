#declar what image to use

FROM python:slim-trixie


RUN apt-get update && apt-get install -y curl && apt-get clean

#create python virtual environment to isollate our python app from system python
RUN python -m venv /opt/venv
ENV PATH=/opt/venv/bin:$PATH

WORKDIR /app

#copy local file to container destination
COPY requirements.txt /tmp/requirements.txt
#run within the container
RUN pip install --no-cache-dir -r /tmp/requirements.txt

#copy local file to container destination
COPY ./src /app





#old comments
#RUN mkdir -p /static_folder
#COPY ./static_html /static_folder

#for demo puroses
#RUN echo "hello world" > index.html



#start python server
CMD ["python", "-m", "http.server", "8000"]

#expose port 8000
#EXPOSE 8000



#docker compose down -v  --remove-orphans
