from quebec_jobs_parser import QuebecProgrammingJobsParser
from sql_database_operations import Database

db = Database()
# uncomment on first execution : will create a database file and a table
#db.create_database()

parser = QuebecProgrammingJobsParser()
parser.execute_and_save()

# prints programming jobs in Quebec city
for row in db.select_10_most_recent_jobs():
    print(row)
