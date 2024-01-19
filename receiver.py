import pika, sys, os


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    # Subscribing a callback function to a queue
    def callback(ch, method, properties, body):
        print(f"[x] Received {body}")


    channel.basic_consume(queue='hello',
                        auto_ack=True,
                        on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CRTL+C')
    channel.start_consuming()


# Loop waits data and runs callback
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
