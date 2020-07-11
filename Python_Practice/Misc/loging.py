import logging

format = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='out.txt', format=format, level=logging.DEBUG)
logging.info('This is a debug message')
