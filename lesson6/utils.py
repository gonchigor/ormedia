import logging
from class_bot import cur_time


def logg_this(message_to_log):
    logging.basicConfig(filename='logs/log' + str(cur_time) + '.log',
                        level=logging.INFO, filemode='w')
    logging.info(message_to_log)
