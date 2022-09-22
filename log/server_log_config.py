import sys
sys.path.append('../')
import logging.handlers
import logging
import os
from general.variables import LOGGING_LEVEL

# создаём формировщик:
server_formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')

# файл для логирования
path = os.path.dirname(os.path.abspath(__file__))
# print(path)
path = os.path.join(path, 'server.log')
# print(path)

# вывод логов
steam = logging.StreamHandler(sys.stderr)
steam.setFormatter(server_formatter)
steam.setLevel(logging.DEBUG)
log_file = logging.handlers.TimedRotatingFileHandler(path, encoding='utf8', interval=1, when='D')
log_file.setFormatter(server_formatter)

# регистратор и его настройки
logger = logging.getLogger('server_dist')
logger.addHandler(steam)
logger.addHandler(log_file)
logger.setLevel(LOGGING_LEVEL)

if __name__ == '__main__':
    logger.critical('Critical event')
    logger.error('Error event')
    logger.debug('Debug event')
    logger.info('Info event')
