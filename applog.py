from loguru import logger


logger.add("./log/{time}.log", rotation="1 week", retention="3 month")
