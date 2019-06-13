from bs4 import BeautifulSoup
import requests
from sql_database_operations import Database

class JobboomParser:
    
    # changed this from 'programmeur' to 'analyste-programmeur' in Quebec City
    # since there are more results that way
    JOBBOOM_QC = 'https://www.jobboom.com/fr/region-de-ville-de-quebec/analyste-programmeur/_r2k-1?displayKeyword=analyste-programmeur&sortBy=relevance'
    JOBBOOM_BASE_URL = 'https://www.jobboom.com'

    def __init__(self):
        self.__database = Database()

    def execute_and_save(self):
        url_list = self.__retrieve_jobboom_jobs()
        self.__save_offers_jobboom(url_list)

    def __retrieve_jobboom_jobs(self):
        response = requests.get(self.JOBBOOM_QC)

        soup = BeautifulSoup(response.content, 'lxml')
        job_ads = soup.findAll('a', href=True)

        # retrieve job posting's url from the list on the first page a/p JOBBOOM_BASE_URL
        # if key word 'description-de-poste' changes, then we need to go back to the 
        # webpage source code 
        #
        url_list = []
        for url_link in job_ads:
            if 'description-de-poste' in url_link['href']:
                url_list.append(self.JOBBOOM_BASE_URL + url_link['href'])

        return url_list

    def __save_offers_jobboom(self, url_list):
        for job_url in url_list:
            response = requests.get(job_url)
            soup = BeautifulSoup(response.content, 'lxml')

            # those Facebook meta-properties contain just the information we want !
            # be opportunist like the fox when scraping the web
            #
            job_title_raw = soup.find('meta', property="og:title")
            job_title = job_title_raw['content']

            self.__database.save(job_title, job_url)
