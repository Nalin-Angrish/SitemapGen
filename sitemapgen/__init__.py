from requests import get
from bs4 import BeautifulSoup
from .helper import *


VERSION = "v0.9.1"
AUTHOR = "Nalin Angrish"
SOURCE = "https://github.com/Nalin-2005/SitemapGen"
AUTHOR_WEBSITE = "https://www.nalinangrish.me"




class Generator():
	def __init__(self, site, output, disguise=None) -> None:
		self.site = site
		if(disguise!=None):
			self.disguise = disguise
		else:
			self.disguise = site
		self.output = output
		
	def genSitemap(self) -> str:
		sitemap = header
		for url in self.urls:
			sitemap += siteFormat.format(str(url), str(timestamp))
		sitemap += footer
		self.sitemap = sitemap
		return sitemap		


	def getLinks(self, path) -> list:
		url = self.site + path
		page = get(url).text
		soup = BeautifulSoup(page, features="html.parser")
		linktags = soup.findAll("a")
		links = []
		for linktag in linktags:
			links.append(linktag["href"])
		return filter(links)

	def discover(self) -> list:
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
		with open(self.output, "w+") as file:
			file.write(self.sitemap)