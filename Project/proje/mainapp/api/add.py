
import logging

logger = logging.getLogger('')

def adding_log(value_type,response_time,timestamp,real_time):
    logger.info(('{},{},{},{}').format(value_type, response_time, timestamp,real_time))
