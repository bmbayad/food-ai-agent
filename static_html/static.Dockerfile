#declar what image to use

FROM python:slim-trixie


WORKDIR /app

COPY ./src /app



#RUN mkdir -p /static_folder
#COPY ./static_html /static_folder

#for demo puroses
#RUN echo "hello world" > index.html



#start python server
#CMD ["python", "-m", "http.server", "8000"]

#expose port 8000
#EXPOSE 8000




