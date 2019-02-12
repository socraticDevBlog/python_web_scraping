import sqlite3
import datetime


class Database:
    DB_NAME = 'jobs_QCity.db'
    DELETE_OFFER_CONTAINING_PROBLEMATIC_WORD_1 = "DELETE FROM jobs_QCity WHERE title LIKE '% programme %'"
    DELETE_OFFER_CONTAINING_PROBLEMATIC_WORD_2 = "DELETE FROM jobs_QCity WHERE title LIKE '% programmes%'"

    # can't rely on URL field to detect duplicates : www.indeed.ca uses 'dynamic' urls
    #
    DEL_DUPLICATES = "DELETE FROM jobs_QCity WHERE rowid NOT IN (SELECT MIN(rowid) FROM jobs_QCity GROUP BY title, description)"
    DEL_EMPTY_RECORD = "DELETE FROM jobs_QCity WHERE title = ''"

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

    def enforce_integrity(self):
        conn = self.__fetch_connection()
        conn.cursor().execute(self.DEL_DUPLICATES)
        conn.cursor().execute(self.DEL_EMPTY_RECORD)
        conn.commit()
        conn.close()

    def remove_probably_irrelevant_offers(self):
        conn = self.__fetch_connection()
        conn.cursor().execute(self.DELETE_OFFER_CONTAINING_PROBLEMATIC_WORD_1)
        conn.cursor().execute(self.DELETE_OFFER_CONTAINING_PROBLEMATIC_WORD_2)
        conn.commit()
        conn.close()

    def __offer_not_in_database(self, connection, title, description, url):
        dataset_count = connection.cursor().execute("SELECT COUNT(*) FROM jobs_QCity WHERE title = ? and description  = ? and url = ?", (title, description, url))
        row_count = dataset_count.fetchone()
        return row_count[0] == 0

    def __fetch_connection(self):
        return sqlite3.connect(self.DB_NAME)
