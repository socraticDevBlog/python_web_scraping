# python_web_scraping

(IF;DR)
this script is hardcoded to fetch job offers for a developer in the area of Quebec City, Canada.
did my best to decouple Data Access from web-scraping logic.

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

2- you can view offers in SQLite3 console, but i prefer using LibreOffice Base for now

3- by geeking out a little what BeautifulSoup library is about, you can switch the 'parsing classes' for your own ; looking for new jobs offering available in your area from your favoriste job websites.

########

code fonctionnel pour illustrer
un tutoriel de web scraping avec
Python et BeautifulSoup

ce code récolte les offres d'emplois pour le rôle de programmeur-analyste dans la région de Québec depuis les sites Jobboom et Indeed
il les enregistre dans une base de données SQLite
il s'assure d'éliminer les duplicats (plusieurs fois la même offre) à chaque exécution

https://maximeboninblog.wordpress.com/2018/08/26/creer-des-api-sur-mesure-avec-la-librairie-beautifulsoup-en-python/

(Dernière mise à jour : jeudi 16 mai 2019)
