import os
import sys
import json
import logging
import argparse


# Log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')


def to_real_key(key):
    if key[0] == '[':
        return int(key[1:-1])
    return key


def get_args():
    parser = argparse.ArgumentParser(description='Ping script')
    parser.add_argument('json_file', action="store")
    parser.add_argument('composite_key', action="store")
    return parser.parse_args()


def get_logger():
    logger_name = os.path.splitext(os.path.basename(__file__))[0]
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.getLevelName(LOG_LEVEL))

    fh = logging.FileHandler(logger_name + ".log")
    fh.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - [%(levelname)s] - %(message)s'))

    logger.addHandler(fh)
    return logger


def get_json_value(json_file, composite_key, logger):
    logger.info("Start")

    json_format = json.load(json_file)
    json_dict = json_format

    single_keys = filter(lambda x: x != '', composite_key.split('.'))
    for i in single_keys:
        try:
            json_dict = json_dict[to_real_key(i)]
        except Exception as e:
            logger.debug(f"There is no key '{i}'")
            logger.exception("%s", e)
            sys.exit(1)

    logger.info("Successful finish!")
    return json.dumps(json_dict, indent=4)


def print_json_value():
    args = get_args()
    logger = get_logger()

    logger.info("Find key: " + args.composite_key)

    with open(args.json_file, "r") as f:
        print(get_json_value(f, args.composite_key, logger))


if __name__ == '__main__':
    print_json_value()
