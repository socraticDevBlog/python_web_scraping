from qc_glassdoor_parser import GlassdoorQcParser
from jobboom_parser import JobboomParser
from indeed_parser import IndeedParser
from sql_database_operations import Database
from sys import argv
from logger import Logger

STEP_JOBBOOM_AND_INDEED = "Getting jobs from Jobbom and Indeed"
STEP_GLASSDOOR = "Getting jobs from Glassdoor"

program_name = argv[0]

# trigger DEBUG logging mode by adding integer param 10 in Terminal
# this way :  $python job_scraper.py 10
#
logger_verbosity_level = int(argv[1]) if len(argv) > 1 else Logger.LOWEST_VERBOSITY
logger = Logger(program_name, logger_verbosity_level)

try:    
    db = Database()
    # uncomment on first execution : will create a database file and a table
    # db.create_database()
except:
    logger.error('unable to create database object')

try:
    print('parsing INDEED website', end = "\r\n")

    parser = IndeedParser(logger)
    parser.execute_and_save()
    
    logger.debug('finished scraping Indeed website' )
except:
    logger.error('unable to execute INDEED')

try:
    print('parsing JOBBOM website', end = "\r\n")

    parser = JobboomParser()
    parser.execute_and_save()
    
    logger.debug('finished scraping JOBBOOM website' )
except:
    logger.error('unable to execute JOBBOOM')

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
