FROM ubuntu:14.04

RUN apt-get update && \
    apt-get install -y \
        curl \
        git \
        python-pip \
        gunicorn

RUN mkdir /home/datatables-view && \
    chown nobody /home/datatables-view

USER nobody
ENV HOME=/home/datatables-view
WORKDIR /home/datatables-view

COPY ./requirements.txt /home/datatables-view/app/
RUN pip install --user -r /home/datatables-view/app/requirements.txt
COPY ./app /home/datatables-view/app/

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000"]
CMD ["app:app"]
