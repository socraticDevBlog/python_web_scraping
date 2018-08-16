from bs4 import BeautifulSoup
import requests
from sql_database_operations import Database


class QuebecProgrammingJobsParser:
    JOBBOOM_QC = 'https://www.jobboom.com/fr/quebec/programmeur-autres/_c23027i10m125-1?sortBy=distance&searchDistance=100'
    BASE_URL = 'https://www.jobboom.com'

    def __init__(self):
        self.__database = Database()

    def execute_and_save(self):
        url_list = self.__retrieve_jobs_url_list()
        self.__parse_indivual_offer_and_save(url_list)

    def __retrieve_jobs_url_list(self):
        response = requests.get(self.JOBBOOM_QC)
        soup = BeautifulSoup(response.content, 'lxml')
        job_ads = soup.findAll('a', href=True)

        url_list = []
        for url_link in job_ads:
            if 'description-de-poste' in url_link['href']:
                url_list.append(self.BASE_URL + url_link['href'])

        return list(url_list)

    def __parse_indivual_offer_and_save(self, url_list):
        for job_url in url_list:
            response = requests.get(job_url)
            soup = BeautifulSoup(response.content, 'lxml')
            job_title_raw = soup.find('meta', property="og:title")
            job_description_raw = soup.find('meta', property="og:description")
            job_title = job_title_raw['content']
            job_description = job_description_raw['content']

            self.__database.save(job_title, job_description, job_url)
