import logging
import datetime


class Logger:

    LOG_FILE = 'log.out'
    
    # logging verbosity can be set from a console command parameter 
    #   ex. : DEBUG verbosity -> $python mainFile.py 10
    #   
    # invokation with parameter = default level of verbosity is ERROR
    #
    # in mainFile, you can parse args this way :
    #
    #       if len(sys.argv) < 2:
    #           obj = Logger(sys.argv[0])
    #       else:
    #           obj = Logger(sys.argv[0], int(sys.argv[1]))

    def __init__(self, program_name, verbosity=logging.ERROR):
        # ERROR level by default = integer of value 40
        # DEBUG level = integer of value 10 inputed by Class user 
        #
        logging.basicConfig(filename=self.LOG_FILE, 
                            level=verbosity
                            )

        # INFO verbosity level is 20 : 
        # only shown when debugging (level 10)
        #
        logging.info('Log for program %s' % program_name)

        now = str(datetime.datetime.today())
        logging.info('Execution date = %s' % now)

    def debug(self, arg):
        logging.debug(arg)

    def error(self, arg):
        now =  str(datetime.datetime.today())
        logging.error(now + ' ' + arg)
    