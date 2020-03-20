# python_web_scraping

This script is hardcoded to fetch job offers for a developer role in the area of Quebec City, Canada.

on first time use (Windows users, i tell you what to do further down):

* make sure to have installed 'BeautifulSoup' library :

  $ sudo apt-get install python3-bs4
  
  $ pip3 install beautifulsoup4

* make sure to have installed the lxml parser library :

   $ sudo apt-get install python3-lxml

* open Main.Py file with a text Editor :

    uncomment the line which will create a SQLite table right next to the code files
    
** You are a poor Windows user ?? no worries ! :

    - Please have Python 3 installed
    
    - If you know how to do it, please put yourself behind a Virtual Environnement (venv)
    
    - via the Command line (PowerShell), install 3 librairies : BeautifulSoup, lxml and Requests
    
        - pip3 install beautifulsoup4
        
        - pip3 install lxml
        
        - pip3 install requests

Then you can expect it to work :

1- just run the jobs_scraper.py file by double-clicking on it and it will fetch job offers in about 30 seconds.

2- you can view offers in SQLite3 console, but i prefer using a web-based tool like 'sqliteonline.com'

3- by geeking out a little what BeautifulSoup library is about, you can switch the 'parsing classes' for your own ; looking for new jobs   
   offering available in your area from your favoriste job websites.
   
 * developers : running script (i.e. 'job_scraper.py') with integer of value 10 will output detailed debug logs in a file named 'log.out'.   (on your terminal start script by typing this : $python job_scraper.py 10) 
