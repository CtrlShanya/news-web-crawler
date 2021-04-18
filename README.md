# Web Crawler for News (SPIEGEL.de)

This is a web crawler that is used to develop a news-database from the SPIEGEL International website: [https://www.spiegel.de/international/](https://www.spiegel.de/international/)

## Motivation

We want to automatically trigger the web crawler to collect relevant news data and store it in our local database every 15 minutes when it is running. 
We want to extract news entries from HTML:
  1)	Subtitle
  2)	Title
  3)	Abstract
  4)	Download Time
  5)	Update Time

![image](https://user-images.githubusercontent.com/58457813/115142881-b8f0e900-a061-11eb-818e-128e90199527.png)

These entries are stored in a SQLite database with the following data format:

`subtitle TEXT NOT NULL PRIMARY KEY, title TEXT, abstract TEXT, download_time TIMESTAMP, update_time TIMESTAMP`

## Technology Stack:

### Built With:

•	Python3 for crawler (`Beautiful soup`, `re`, `requests`, `time`, `sys`, `unidecode`, `datetime`)

•	SQLite for Data Storage (`sqlite3`)

# Features:

•	This crawler can handle duplicate entries, different containers for news articles and also collect data from articles that may have missing Abstract, etc.

•	It can also be used on any of the 500 pages of the SPIEGEL International website, we just need to edit the `url` as shown: 

  `https://www.spiegel.de/international/p{$PAGE_NUMBER}/`
  
  For example: For page 2: `https://www.spiegel.de/international/p2/`
  
  The rest of the code will work just as before after updating the URL.

• This crawler automatically run every 15 minutes, till the user stops the code when prompted to continue.

This program while running, may ask the user the following:
      `Do you want to continue (enter 'y' or 'n'):`
This is to stop the program as per the user's wishes. So to stop the program, please enter: `n` and to keep the program running, please enter: `y`.

# Installation:

1)	Download the zip folder from git clicking on `Code` as shown:

    ![image](https://user-images.githubusercontent.com/58457813/115142981-39afe500-a062-11eb-8e7d-207f325b6f98.png)
    
2)  Extract files from the zip folder downloaded. (Please make sure to keep the database file: `News.db` in the same folder as the code files)

3)  Open the `Command Prompt` on your local machine, in the folder with the extracted code files, and download the required libraries by running the `requirements.txt` as shown in the command prompt:
    `pip install -r requirements.txt`

# How to Use?

1)  Then run the `Crawler.py` file to start the crawler as shown: (Input)
    `python Crawler.py`

2)  To view the contents of the table `test1` run the following on the Command Prompt: (Output)
    `python Database.py`



