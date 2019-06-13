from bs4 import BeautifulSoup
import requests
from sql_database_operations import Database


class GlassdoorQcParser:
    
    # it used to look for the word 'programmer' which gives us garbage and game development jobs
    # let's try 'analyste-programmeur' in Quebec City 
    # date is : May 16th 2019
    # 
    GLASSDOOR_QC = "https://www.glassdoor.ca/Job/quebec-analyste-programmeur-jobs-SRCH_IL.0,6_IC2298450_KO7,27.htm"
    GLASSDOOR_BASE_URL = "https://www.glassdoor.ca"

    def __init__(self):
        self.__database = Database()

    def execute_and_save(self):
        jobs = self.__glassdoor_jobs()
        urls = self.__glassdoor_jobs_url()
        self.__save_offers_glassdoor(jobs, urls)

    def __glassdoor_jobs(self):
        titles = []
        for item in self.__soup():
            titles.append(item.text)

        return list(titles)

    def __glassdoor_jobs_url(self):
        url_list = []
        for item in self.__soup():
            url_list.append(self.GLASSDOOR_BASE_URL + item['href'])

        return list(url_list)

    def __save_offers_glassdoor(self, jobs, urls):
        for key, value in dict(zip(jobs, urls)).items():
            self.__database.save(key, value)

    def __response(self):
        # website refuses connection to a crawler agent (HTTP error 403)
        # assign a phony agent to the Request
        #
        return requests.get(self.GLASSDOOR_QC,  headers={'User-Agent': 'Mozilla/5.0'})

    def __soup(self):
        # the 'soup' is a list of all html 'a' tags of class 'joblink'
        # them Glassdoor have us working over time to get what we want !!
        #
        soup = BeautifulSoup(self.__response().content, 'lxml')
        return soup.findAll("a", {"class": "jobLink"})
