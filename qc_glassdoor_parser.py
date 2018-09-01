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
        # website refuses connection to a crawler agent (HTTP error 403)
        # assign a phony agent to the Request
        #
        agent = 'Mozilla/5.0'
        response = requests.get(self.GLASSDOOR_QC,  headers={'User-Agent': agent})
        soup = BeautifulSoup(response.content, 'lxml')
        job_title = soup.findAll("a", {"class": "jobLink"})

        titles = []
        for title in job_title:
            titles.append(title.text)

        return list(titles)

    def __retrieve_glassdoor_jobs_url(self):
        agent = 'Mozilla/5.0'
        response = requests.get(self.GLASSDOOR_QC,  headers={'User-Agent': agent})
        soup = BeautifulSoup(response.content, 'lxml')
        job_ads = soup.findAll("a", {"class": "jobLink"})

        url_list = []
        for url_link in job_ads:
            url_list.append(self.GLASSDOOR_BASE_URL + url_link['href'])

        return list(url_list)

    def __save_offers_glassdoor(self, jobs, urls):
        temp_dict_job_url = dict(zip(jobs, urls))

        for key, value in temp_dict_job_url.items():
            self.__database.save(key, 'unavailable due to hard to parse HTML ;)', value)
