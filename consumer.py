import pika
import json
import os

RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST', 'localhost')
RABBITMQ_PORT = os.environ.get('RABBITMQ_PORT', 5672)
RABBITMQ_USERNAME = os.environ.get('RABBITMQ_USERNAME', 'guest')
RABBITMQ_PASSWORD = os.environ.get('RABBITMQ_PASSWORD', 'guest')
RABBITMQ_QUEUE = 'event_notifications'


def callback(ch, method, properties, body):
    print(f"Received {body}")
    data = json.loads(body)
    for participant in data['participants']:
        print(f"Sending reminder to {participant}")
        # ----------------- Send email to participant -----------------
        # ----------------- use email service logic or API -----------------

    print(f"Sent reminder for event '{data['event_name']}' to {len(data['participants'])} participants.")
    ch.basic_ack(delivery_tag=method.delivery_tag)


def consumer():
    credentials = pika.PlainCredentials(RABBITMQ_USERNAME, RABBITMQ_PASSWORD)
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)
    channel.basic_consume(queue=RABBITMQ_QUEUE, on_message_callback=callback, auto_ack=False)

    print("Starting consumer. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == '__main__':
    consumer()
