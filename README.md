# news-webcrawler
This python script works as a service for my other repository the <a href='https://github.com/benderFF98/news-api'>News API<a>.
This script can run the webcrawlers created inside the crawler_functions.py an save the 5 top articles to the API database using an API Post Request.
To test it you need to clone the API Repository, run the project and migrate the database, the .env is already configured for the path it should, but if you change the port on the other project, do it in this one as well.
To run the crawler you need to run the following command: 
```shell
python3 main.py --crawler_name
```
Example:
```shell
python3 main.py --tabnews
```
