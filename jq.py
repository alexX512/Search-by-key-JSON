import sys
import os
import json
import logging


# Log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_LEVEL = os.environ['LOG_LEVEL'] if 'LOG_LEVEL' in os.environ else "INFO"


def to_real_key(key):
    if key[0] == '[':
        return int(key[1:-1])
    return key


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.getLevelName(LOG_LEVEL))
    fh = logging.FileHandler(name + ".log")
    fh.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - [%(levelname)s] - %(message)s'))
    logger.addHandler(fh)
    return logger


logger_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
logger = get_logger(logger_name)

json_file = sys.argv[1]
composite_key = sys.argv[2]
logger.info("Find key: " + composite_key)

with open(json_file, "r") as f:
    logger.info("Start")
    json_format = json.load(f)
    json_dict = json_format
    single_keys = filter(lambda x: x != '', composite_key.split('.'))
    for i in single_keys:
        try:
            json_dict = json_dict[to_real_key(i)]
        except Exception as e:
            logger.debug("There is no key '" + i + "'")
            logger.exception("%s", e)
            sys.exit(1)
    print(json.dumps(json_dict, indent=4))
    logger.info("Successful finish!")
