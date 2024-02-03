# Consumer Service

This service is a simple consumer that listens to a RabbitMQ queue and processes the messages. It's written in Python and uses the `pika` library to interact with RabbitMQ.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.9
- Docker
- RabbitMQ server

### Installing

1. Clone the repository
2. Navigate to the project directory
3. Build the Docker image:

```bash
docker build -t consumer-service .
```

4. Run the Docker container:

```bash
docker run -d --name consumer-service consumer-service
```

## Usage

The consumer service is designed to listen to a RabbitMQ queue and process incoming messages. The messages are expected to be in JSON format with the following structure:

```json
{
  "event_name": "Event Name",
  "participants": ["participant1@example.com", "participant2@example.com"]
}
```

The service will print the received message and send a reminder to each participant.

## Environment Variables

The service uses the following environment variables:

- `RABBITMQ_HOST`: The hostname of the RabbitMQ server. Default is `localhost`.
- `RABBITMQ_PORT`: The port number of the RabbitMQ server. Default is `5672`.
- `RABBITMQ_USERNAME`: The username to connect to the RabbitMQ server. Default is `guest`.
- `RABBITMQ_PASSWORD`: The password to connect to the RabbitMQ server. Default is `guest`.

## Built With

- [Python](https://www.python.org/)
- [pika](https://pypi.org/project/pika/)
- [Docker](https://www.docker.com/)

## Authors

- [galnaaman](https://github.com/galnaaman)

## License

This project is licensed under the MIT License.