import logging
from logstash_async.handler import AsynchronousLogstashHandler

from flask import Flask, jsonify


logger = logging.getLogger('ELK-test')
logger.setLevel(logging.INFO)
logstash_formatter = logging.Formatter(
    fmt=' %(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logstash_handler = AsynchronousLogstashHandler('0.0.0.0', 5002, database_path=None)
logstash_handler.setFormatter(logstash_formatter)
logger.addHandler(logstash_handler)

app = Flask(__name__)


@app.route('/hello/<name>')
def saly_hello(name):
    logger.info('Hello, {}!'.format(name))
    return jsonify({'message': 'Hello, {}!'.format(name)})


@app.route('/')
def app_info():
    logger.info('This is a simple Flask app')
    return jsonify({'message': 'This is a simple Flask app'})


if __name__ == '__main__':
    logger.info('Starting the app')
    app.run(debug=True, host='0.0.0.0', port=5001)
