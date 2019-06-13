from bs4 import BeautifulSoup
import requests
from sql_database_operations import Database
from logger import Logger


class IndeedParser:
    
    # i've checked this URL as of :  may 16th 2019
    INDEED_QC = 'https://www.indeed.ca/programmeur-jobs-in-Quebec-City'
    INDEED_BASE_URL = 'https://www.indeed.ca'
    PRETEND_TO_BE_A_BROWSER = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
   
   # note the trailing space ... !
   #
    CLASS_WHERE_URL_IS = "jobtitle turnstileLink "

    def __init__(self, passed_logger):        
        self._logger = passed_logger

        try:
            self.__database = Database()

            self._logger.debug("Created database")
        except:
           self._logger.error("failed to create database")
        
    def execute_and_save(self):
        url_list = self.__retrieve_indeed_jobs()
        self.__save_offers_indeed(url_list)

    def __retrieve_indeed_jobs(self):
        url = self.INDEED_QC    
        headers = {'User-Agent': self.PRETEND_TO_BE_A_BROWSER}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'lxml')
        job_ads = soup.findAll("a", {"class": self.CLASS_WHERE_URL_IS})

        url_list = []
        for url_link in job_ads:
            the_url = self.INDEED_BASE_URL + url_link['href']
            url_list.append(the_url)

        return list(url_list)

    def __save_offers_indeed(self, url_list):
        for job_url in url_list:
            response = requests.get(job_url)
            soup = BeautifulSoup(response.content, 'lxml')
            job_title = soup.title.text
            job_description = soup.find("meta",  property="content")
            

            # BeautifulSoup is unable to retrieve the whole html document -
            # probably due to syntax error in the <body> ...
            # thus save what you're able to retrieve !
            #
            self.__database.save(job_title, job_url)
