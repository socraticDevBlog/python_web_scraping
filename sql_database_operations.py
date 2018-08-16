import sqlite3
import datetime


class Database:
    DB_NAME = 'jobs_QCity.db'
    QC_ALL_JOBS_TABLE = 'SELECT * FROM jobs_QCity'
    QC_RECENT_JOBS_TABLE = 'SELECT * FROM (SELECT * FROM jobs_QCity ORDER BY id DESC LIMIT 10) ORDER BY id ASC'

    def select_10_most_recent_jobs(self):
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
        conn.cursor().execute(sql, (title, description, url, insertion_date))
        conn.commit()
        conn.close()

    def __fetch_connection(self):
        return sqlite3.connect(self.DB_NAME)
