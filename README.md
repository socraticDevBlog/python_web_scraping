# python_web_scraping

This script is hardcoded to fetch job offers for a developer role in the area of Quebec City, Canada.

on first time use :

* make sure to have installed 'BeautifulSoup' library :

  $ sudo apt-get install python3-bs4
  
  $ pip install bs4

* make sure to have installed the lxml parser library :

   $ sudo apt-get install python3-lxml

* open Main.Py file with a text Editor :

    uncomment the line which will create a SQLite table right next to the code files

Then you can expect it to work :

1- just run the Main.Py file by double-clicking on it and it will fetch job offers in about 30 seconds.

2- you can view offers in SQLite3 console, but i prefer using a web-based tool like 'sqliteonline.com'

3- by geeking out a little what BeautifulSoup library is about, you can switch the 'parsing classes' for your own ; looking for new jobs   
   offering available in your area from your favoriste job websites.
