import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare recipient queue
channel.queue_declare(queue='hello')

# Specify to which queue the message should go
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Helu helu')
print(" [x] Sent 'Helu helu'")

connection.close()