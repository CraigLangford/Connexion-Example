FROM python:3.6-alpine

WORKDIR /app

COPY . .
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]
