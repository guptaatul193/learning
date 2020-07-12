import logging, sys

# setting file handler configurations
log_fl_handler = logging.FileHandler(filename='argument_log.txt')
log_fl_handler.setLevel(logging.DEBUG)
log_fl_handler.setFormatter(logging.Formatter('%(asctime)s\t%(message)s'))

# creating and setting logger configurations
log_logger = logging.getLogger('argument_log')
log_logger.setLevel(logging.DEBUG)
log_logger.addHandler(log_fl_handler)

inp_cli = sys.argv[1]

log_logger.info(inp_cli)
