from quebec_jobs_parser import QuebecProgrammingJobsParser
from qc_glassdoor_parser import GlassdoorQcParser
from sql_database_operations import Database
from sys import argv
from logger import Logger

STEP_JOBBOOM_AND_INDEED = "Getting jobs from Jobbom and Indeed"
STEP_GLASSDOOR = "Getting jobs from Glassdoor"

program_name = argv[0]
logger_verbosity_level = int( argv[1]) if len(argv) > 1 else Logger.LOWEST_VERBOSITY
logger = Logger(program_name, logger_verbosity_level)

try:    
    db = Database()
    # uncomment on first execution : will create a database file and a table
    #db.create_database()
except:
    logger.error('unable to create database object')

try:
    print(STEP_JOBBOOM_AND_INDEED, end = "\r\n")
    parser = QuebecProgrammingJobsParser()
    parser.execute_and_save()
    
    logger.debug('finished scraping Joboom and Indeed websites' )
except:
    logger.error('scraping Jobboom or Indeed websites')

try:
    print(STEP_GLASSDOOR, end = "\r\n")
    glassdoor_parser = GlassdoorQcParser()
    glassdoor_parser.execute_and_save()

    logger.debug('finished scraping Glassdoor website' )
except:
    logger.error('scraping Glassdoor website')

try:
    print("Getting rid of duplicate rows", end = "\r\n")
    db.enforce_integrity()

    logger.debug('finished getting rid of duplicate rows' )
except:
    logger.error('getting rid of duplicate rows')

try:
    print("Removing irrelevant job offers", end = "\r\n")
    db.remove_probably_irrelevant_offers()

    logger.debug('finished removing irrelevant offers' )
except:
    logger.error('removing probably irrelevant offers')
