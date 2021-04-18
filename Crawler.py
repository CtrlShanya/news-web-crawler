import datetime
import requests
import re
import sqlite3
import sys
import time
import unidecode

from bs4 import BeautifulSoup

WAITTIME = 900
TIMEOUT = 20

def divCrawler(div, cursor):
	"""
	To crawl each div container and to store the data in an SQLite table.
	:param div: div container to crawl
	:param cursor: cursor to the SQLite database
	
	:type div: Python3 list
	:type cursor: sqlite3.Cursor
	
	This function does not return any value.
	"""

	# choosing tags on the basis of class names formatting, while using 're' for partial class name matching
	for d in div:
		
		# subtitles
		subtitle = d.find('span', class_=re.compile(r"^block text-primary-base"))
		if not subtitle:
			subtitle = d.find('span', class_=re.compile(r"^focus:text-primary-darker"))
		subtitle = unidecode.unidecode(subtitle.get_text(strip=True))
		
		# Big and italic titles
		title = d.find('span', class_=re.compile(r"^align-middle hover:opacity-moderate"))
		if not title:
			# normal titles
			title = d.find('span', class_=re.compile(r"^block font-sansUI font-bold text-xl"))
		if not title:
			# italic titles
			title = d.find('span', class_=re.compile(r"^italic align-middle hover:opacity-moderate"))
		title = unidecode.unidecode(title.get_text(strip=True))
		
		# abstract
		abstract = d.find('span', class_=re.compile(r"^font-serifUI"))
		if abstract:
			abstract = unidecode.unidecode(abstract.get_text(strip=True))
		else:
			abstract = '-'
		
		# download time
		d_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		# update time
		u_time = '-'
		
		if title and subtitle:
			try:
				cursor.execute("INSERT INTO test1 VALUES (?,?,?,?,?);", (subtitle, title, abstract, d_time,u_time))
			except sqlite3.IntegrityError as error:
				# for data already stored in our table, we just need to update time
				u_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
				cursor.execute("UPDATE test1 SET update_time=? WHERE subtitle=?", (u_time, subtitle))

def crawler(cursor):
	"""
	To crawl the given URL every 15 minutes, till the program is asked to stop.
	
	:param cursor: cursor to the SQLite database
	:type cursor: sqlite3.Cursor
	
	This function does not return any value.
	"""

	url="https://www.spiegel.de/international/"
	# code can cover all pages of SPIEGEL International, we just need an additional loop for the remaining 500 pages
	status = None
	while True:
		try:
			status = requests.get(url)
			break
		except requests.exceptions.ConnectionError as req:
			print("Retrying request to URL...")
			time.sleep(TIMEOUT)
		
	html_content = status.text
	soup = BeautifulSoup(html_content, "lxml")
	
	# two types of containers need different lists:
	div_tag_1 = soup.findAll('div', {'class':'z-10 w-full'})
	div_tag_2 = soup.findAll('div', {'class':re.compile(r'^z-10 lg:w-4/12')})
	
	# crawling each container
	divCrawler(div_tag_1, cursor)
	divCrawler(div_tag_2, cursor)
	
	# commiting changes to database on local machine
	connection.commit()
	
	# to stop the code by command: 'y' for continuing and 'n' to stop the code
	answer = input("Do you want to continue (enter 'y' or 'n'): ")
	if answer == "n":
		sys.exit("Exiting program now...")
		
	# 15 minutes of waiting time
	time.sleep(WAITTIME)
	crawler(cursor)
	
############################## MAIN ############################

# creating a connection to the Database
connection = sqlite3.connect("News.db")
cursor = connection.cursor()

# Calling the Crawler
crawler(cursor)

# closign connection to the Database
connection.close()