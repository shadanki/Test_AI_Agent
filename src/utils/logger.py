import logging

def setup_logger(name: str = __name__):
  logger = logging.getLogger(name)
  handler = logging.StreamHandler()
  formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
  handler.setFormatter(formatter)
  logger.setLevel(logging.INFO)
  logger.addHandler(handler)
  return logger