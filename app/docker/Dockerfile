FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# requirements python
COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN apt-get update \
    && apt-get install -y \
        netcat-traditional
# copy all the code
COPY . .

EXPOSE 8000

ENTRYPOINT ["docker/entrypoint.sh"]
