from quebec_jobs_parser import QuebecProgrammingJobsParser
from qc_glassdoor_parser import GlassdoorQcParser
from sql_database_operations import Database

db = Database()
# uncomment on first execution : will create a database file and a table
db.create_database()

print("Getting jobs from Jobbom and Indeed")
parser = QuebecProgrammingJobsParser()
parser.execute_and_save()

print("")
print("Getting jobs from Glassdoor")
glassdoor_parser = GlassdoorQcParser()
glassdoor_parser.execute_and_save()

print("")
print("Getting rid of duplicate rows")
db.enforce_integrity()

print("")
print("Removing irrelevant job offers")
db.remove_probably_irrelevant_offers()
