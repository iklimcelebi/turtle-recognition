import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def info(msg):
    logging.info(msg)

def error(msg):
    logging.error(msg)

def debug(msg):
    logging.debug(msg)