import logging

#---------------------
# Basic Logging
#------------------
# Greate for platforms that manage logs for you
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.debug("debbuging message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")

#--------------------
# BasicConfig Logging
#--------------------
# For when you want to manage your own log file & message format
logging.basicConfig(
        level=logging.DEBUG,
        filename='log_file.log',
        datefmt="%d-%m-%Y %H:%M:%S",
        # format='{"time": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}'
        format='%(asctime)s %(levelname)s %(message)s'
        )
logging.debug("debbuging message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")