import socket

from flask import Flask
import redis

import config

app = Flask(__name__)

if socket.gethostname() == 'GXMBP.local':
    app.config.from_object(config.DevelopmentConfig)
elif socket.gethostname() == 'iZ23bo17lpkZ':
    app.config.from_object(config.ProductionConfig)
else:
    app.config.from_object(config.TestingConfig)

redis_conf = app.config.get('REDIS_CONF')
pool = redis.ConnectionPool(host=redis_conf.host, port=redis_conf.port, db=redis_conf.db)
r_session = redis.Redis(connection_pool=pool)

from tools import *
from excavator import *

if __name__ == '__main__':
    app.run()
