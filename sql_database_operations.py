import sqlite3
import datetime


class Database:
    DB_NAME = 'jobs_QCity.db'
    QC_ALL_JOBS_TABLE = 'SELECT * FROM jobs_QCity'
    QC_RECENT_JOBS_TABLE = 'SELECT * FROM (SELECT * FROM jobs_QCity ORDER BY id DESC LIMIT 20) ORDER BY id ASC'

    # can't rely on URL field to detect duplicates : www.indeed.ca uses 'dynamic' urls
    #
    DEL_DUPLICATES = "DELETE FROM jobs_QCity WHERE rowid NOT IN (SELECT MIN(rowid) FROM jobs_QCity GROUP BY title, description)"
    DEL_EMPTY_RECORD = "DELETE FROM jobs_QCity WHERE title = ''"

    def select_20_most_recent_jobs(self):
        return self.__select(self.QC_RECENT_JOBS_TABLE)

    def select_all_jobs_qcity(self):
        return self.__select(self.QC_ALL_JOBS_TABLE)

    def __select(self, sql):
        conn = self.__fetch_connection()
        table = conn.cursor().execute(sql)
        rows = list(table)
        conn.close()
        return rows

    def create_database(self):
        table_creation_sql = (" CREATE TABLE IF NOT EXISTS jobs_QCity(\n"
                              "     id integer PRIMARY KEY,\n"
                              "     title VARCHAR ,\n"
                              "     description TEXT,\n"
                              "     url VARCHAR,\n"
                              "     insert_date TEXT\n"
                              "     ); ")

        conn = self.__fetch_connection()
        conn.cursor().execute(table_creation_sql)
        conn.commit()
        conn.close()

    def save(self, title, description, url):
        sql = "INSERT INTO jobs_QCity (title, description, url, insert_date) VALUES(?, ?, ?, ?)"
        insertion_date = datetime.datetime.now()
        conn = self.__fetch_connection()

        if self.__offer_not_in_database(conn, title, description, url):
            conn.cursor().execute(sql, (title, description, url, insertion_date))
            conn.commit()
            conn.close()

    def __offer_not_in_database(self, connection, title, description, url):
        dataset_count = connection.cursor().execute("SELECT COUNT(*) FROM jobs_QCity WHERE title = ? and description  = ? and url = ?", (title, description, url))
        row_count = dataset_count.fetchone()
        return row_count[0] == 0

    def enforce_integrity(self):
        conn = self.__fetch_connection()
        conn.cursor().execute(self.DEL_DUPLICATES)
        conn.cursor().execute(self.DEL_EMPTY_RECORD)
        conn.commit()
        conn.close()

    def __fetch_connection(self):
        return sqlite3.connect(self.DB_NAME)
