# python_web_scraping

(IFDR;)
this script is hardcoded to fetch job offers for a developer in the area of Quebec City, Canada.
did my best to decouple Data Access from web-scraping logic.

on first time use :

1- open Main.Py file and uncomment the line which will create a SQLite table right next to the code files

2- just run the Main.Py file by double-clicking on it and it will fetch job offers in about 30 seconds.

3- you can view offers in SQLite3 console, but i prefer using LibreOffice Base for now

4- by geeking out a little what BeautifulSoup library is about, you can switch the 'parsing classes' for your own ; looking for new jobs offering available in your area from your favoriste job websites.

########

code fonctionnel pour illustrer
un tutoriel de web scraping avec
Python et BeautifulSoup

ce code récolte les offres d'emplois pour le rôle de programmeur-analyste dans la région de Québec depuis les sites Jobboom et Indeed
il les enregistre dans une base de données SQLite
il s'assure d'éliminer les duplicats (plusieurs fois la même offre) à chaque exécution

https://maximeboninblog.wordpress.com/2018/08/26/creer-des-api-sur-mesure-avec-la-librairie-beautifulsoup-en-python/

(Dernière mise à jour : dimanche 26 août 2018)
