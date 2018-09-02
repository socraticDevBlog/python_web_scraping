from bs4 import BeautifulSoup
import requests
from sql_database_operations import Database


class GlassdoorQcParser:
    GLASSDOOR_QC = "https://www.glassdoor.ca/Job/quebec-programmer-jobs-SRCH_IL.0,6_IC2298450_KO7,17.htm"
    GLASSDOOR_BASE_URL = "https://www.glassdoor.ca"

    def __init__(self):
        self.__database = Database()

    def execute_and_save(self):
        jobs = self.__retrieve_glassdoor_jobs()
        urls = self.__retrieve_glassdoor_jobs_url()
        self.__save_offers_glassdoor(jobs, urls)

    def __retrieve_glassdoor_jobs(self):
        titles = []
        for item in self.__retrieve_soup():
            titles.append(item.text)

        return list(titles)

    def __retrieve_glassdoor_jobs_url(self):
        url_list = []
        for item in self.__retrieve_soup():
            url_list.append(self.GLASSDOOR_BASE_URL + item['href'])

        return list(url_list)

    def __retrieve_soup(self):
        soup = BeautifulSoup(self.__response().content, 'lxml')
        return soup.findAll("a", {"class": "jobLink"})

    def __save_offers_glassdoor(self, jobs, urls):
        for key, value in dict(zip(jobs, urls)).items():
            self.__database.save(key, 'unavailable due to hard to parse HTML ;)', value)

    def __response(self):
        # website refuses connection to a crawler agent (HTTP error 403)
        # assign a phony agent to the Request
        #
        return requests.get(self.GLASSDOOR_QC,  headers={'User-Agent': 'Mozilla/5.0'})
