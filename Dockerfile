FROM python:3.10.0

COPY . /app
WORKDIR ./app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]