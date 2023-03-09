import threading
import flask
import logging
from kafka import KafkaConsumer, KafkaProducer

KAFKA_SERVER = 'kafka:9092'

app = flask.Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


def consume():
    consumer = KafkaConsumer('add_to_basket', group_id='python-group', enable_auto_commit=False,
                             bootstrap_servers=['kafka:9092'], api_version=(0, 9))

    for message in consumer:
        print("Received Message in topic - add_to_basket " , message.value)


# def produce():
#     producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
#
#     def on_error(exception):
#         raise Exception(exception)
#
#     producer.send('add_to_basket', b'Hello').add_errback(on_error)
#     producer.flush()


@app.route('/', methods=['GET'])
def home():
    return 'Hello Flask'


thread = threading.Thread(target=consume)

thread.start()

app.run(host='0.0.0.0', port=83)
