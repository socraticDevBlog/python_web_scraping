import datetime
import time
import logging


class Logger:

    LOG_FILE = 'log_'
    TIMESTAMP_SYNTAX = "%Y%m%d-%H%M%S"
    FILE_TYPE = '.out'
    LOWEST_VERBOSITY = logging.ERROR
    
    def __init__(self, program_name, verbosity=LOWEST_VERBOSITY):
        now = str(datetime.datetime.today())

        timestamp = time.strftime(self.TIMESTAMP_SYNTAX)
        log_file_name = self.LOG_FILE + timestamp  + self.FILE_TYPE

        logging.basicConfig(filename=log_file_name, 
                            level=verbosity
                            )

        logging.critical('Log for program %s' % program_name)
        logging.critical('Execution date = %s' % now)

    def debug(self, arg):
        logging.debug(arg)

    def error(self, arg):
        now =  str(datetime.datetime.today())
        logging.error(now + ' ' + arg)
    