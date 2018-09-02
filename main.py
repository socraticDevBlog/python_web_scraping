from quebec_jobs_parser import QuebecProgrammingJobsParser
from qc_glassdoor_parser import GlassdoorQcParser
from sql_database_operations import Database

db = Database()
# uncomment on first execution : will create a database file and a table
#db.create_database()

parser = QuebecProgrammingJobsParser()
parser.execute_and_save()

glassdoor_parser = GlassdoorQcParser()
glassdoor_parser.execute_and_save()

db.enforce_integrity()
