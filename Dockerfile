FROM python:3.9-slim
WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

ENV RABBITMQ_HOST=host.docker.internal
ENV RABBITMQ_PORT=5672
ENV RABBITMQ_USERNAME=guest
ENV RABBITMQ_PASSWORD=guest


CMD ["python", "consumer.py"]
