from bs4 import BeautifulSoup
import requests
from sql_database_operations import Database

class QuebecProgrammingJobsParser:
    
    # i've checked this URL as of :  may 16th 2019
    INDEED_QC = 'https://www.indeed.ca/jobs?q=programmeur&l=Qu%C3%A9bec+City%2C+QC'
    INDEED_BASE_URL = 'https://www.indeed.ca'

    # changed this from 'programmeur' to 'analyste-programmeur' in Quebec City
    # since there are more results that way
    JOBBOOM_QC = 'https://www.jobboom.com/fr/region-de-ville-de-quebec/analyste-programmeur/_r2k-1?displayKeyword=analyste-programmeur&sortBy=relevance'
    JOBBOOM_BASE_URL = 'https://www.jobboom.com'

    def __init__(self):
        self.__database = Database()

    def execute_and_save(self):
        url_list = self.__retrieve_jobboom_jobs()
        self.__save_offers_jobboom(url_list)
        url_list = self.__retrieve_indeed_jobs()
        self.__save_offers_indeed(url_list)

    def __retrieve_jobboom_jobs(self):
        response = requests.get(self.JOBBOOM_QC)

        # see 'lxml' :  you will have to install the lxml python's library in your environment
        # hint : you will use PIP
        #
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

    def __retrieve_indeed_jobs(self):
        response = requests.get(self.INDEED_QC)
        soup = BeautifulSoup(response.content, 'lxml')
        job_ads = soup.findAll("a", {"class": "jobtitle turnstileLink"})

        url_list = []
        for url_link in job_ads:
            url_list.append(self.INDEED_BASE_URL + url_link['href'])

        return list(url_list)

    def __save_offers_jobboom(self, url_list):
        for job_url in url_list:
            response = requests.get(job_url)
            soup = BeautifulSoup(response.content, 'lxml')

            # those Facebook meta-properties contain just the information we want !
            # be opportunist like the fox when scraping the web
            #
            job_title_raw = soup.find('meta', property="og:title")
            job_description_raw = soup.find('meta', property="og:description")
            job_title = job_title_raw['content']
            job_description = job_description_raw['content']

            self.__database.save(job_title, job_description, job_url)

    def __save_offers_indeed(self, url_list):
        for job_url in url_list:
            response = requests.get(job_url)
            indeed_soup = BeautifulSoup(response.content, 'lxml')
            job_title = indeed_soup.title.text

            # BeautifulSoup is unable to retrieve the whole html document -
            # probably due to syntax error in the <body> ...
            # thus save what you're able to retrieve !
            #
            self.__database.save(job_title, "unavailable - crappy html", job_url)
