import sys
import os
sys.path.append('../')
import logging
from general.variables import LOGGING_LEVEL

# создаём формировщик:
client_formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')

# файл для логирования
path = os.path.dirname(os.path.abspath(__file__))
# print(path)
path = os.path.join(path, 'client.log')
# print(path)

# вывод логов
steam = logging.StreamHandler(sys.stderr)
steam.setFormatter(client_formatter)
steam.setLevel(logging.ERROR)
log_file = logging.FileHandler(path, encoding='utf8')
log_file.setFormatter(client_formatter)

# регистратор и его настройки
logger = logging.getLogger('client_dist')
logger.addHandler(steam)
logger.addHandler(log_file)
logger.setLevel(LOGGING_LEVEL)

if __name__ == '__main__':
    logger.critical('Critical event')
    logger.error('Error event')
    logger.debug('Debug event')
    logger.info('Info event')
