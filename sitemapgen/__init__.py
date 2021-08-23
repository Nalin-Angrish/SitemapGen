"""
The main importing entry point for the library 
"""

import cloudscraper
get = cloudscraper.create_scraper().get
from bs4 import BeautifulSoup
from .helper import *


VERSION = "v0.9.7"
AUTHOR = "Nalin Angrish"
SOURCE = "https://github.com/Nalin-2005/SitemapGen"
AUTHOR_WEBSITE = "https://www.nalinangrish.me"




class Generator():
	"""A Class that is used to generate sitemaps from a website's URL and output it as a string or write it to a file.
	"""
	def __init__(self, site, output, disguise=None) -> None:
		"""The constructer for the class

		Args:
			**site** (str): The URL of the website to build a sitemap of.
			**output** (str): The path of the output sitemap file.
			**disguise** (str, optional): To set a disguise the sitemap's URL, which is best suited to generate sitemap of a localhost website which needs to be deployed. Defaults to None.
		"""
		self.site = prepare(site)
		if(disguise!=None):
			self.disguise = disguise
		else:
			self.disguise = site
		self.output = output
		

	def genSitemap(self) -> str:
		"""A function to generate a sitemap and return a copy of the same to the user. Must only be used after `Generator.discover()`

		Returns:
			**str**: The string version of the generated sitemap.
		"""
		sitemap = header
		for url in self.urls:
			sitemap += siteFormat.format(str(url), str(timestamp))
		sitemap += footer
		self.sitemap = sitemap
		return sitemap		


	def getLinks(self, path) -> list:
		"""A function to get the available hyperlinks from the website

		Args:
			**path** (str): The path of the webpage after the domain.

		Returns:
			**list**: All links that could be extracted from the webpage.
		"""
		url = self.site + path
		response = get(url)
		page = response.text
		soup = BeautifulSoup(page, features="html.parser")
		linktags = soup.findAll("a")
		links = []
		for linktag in linktags:
			try:
				links.append(rectify(linktag["href"], response.url, path))
			except:
				pass
		return list(dict.fromkeys(links))

	def discover(self) -> list:
		"""A function to discover all the hyperlinks and the pages available on the domain.

		Returns:
			**list**: A list of all URLs from a website
		"""
		urls = []
		links = self.getLinks("/")
		passed = []
		left = True
		while(left):
			left = False
			xlinks = []
			for link in links:
				if link not in passed:
					urls.append(self.disguise+link)
					xlinks.extend(self.getLinks(link))
					passed.append(link)
					left = True
			links = xlinks
		
		self.urls = urls
		return urls

	def write(self):
		"""Write the sitemap content to the specified output file.
		"""
		with open(self.output, "w+") as file:
			file.write(self.sitemap)