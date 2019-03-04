import logging
import json


logging.basicConfig(level=logging.DEBUG, filename='change.log')
logger = logging.getLogger('change_log')

with open('test.json') as f:
    data = json.loads(f.read())
    logger.info(data.get('name', 'not found'))