from datetime import date




siteFormat = """
<url>
<loc>{}</loc>
<lastmod>{}</lastmod>
<priority>1</priority>
</url>
"""
header = '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">\n<!-- Made using SitemapGen - By Nalin Angrish -->'
footer = "</urlset>"
timestamp = date.today()







def filter(array):
	links = list(dict.fromkeys(array))
	finalLinks = []
	for link in links:
		if((not str(link).startswith("http")) and (not ":" in str(link)) and (not str(link).startswith("#"))):
			if(link.startswith("/")):
				finalLinks.append(link)
			else:
				finalLinks.append("/"+link)
	return finalLinks




def displayHelpMessage(VERSION):
	print(f"""SitemapGen {VERSION} - By Nalin Angrish.
A general utility script for generating site XML sitemaps.

Options:
  --version        | Show the tool version
  --help           | Show this message and exit.
  --url <url>      | Specify a website url to generate a sitemap from. 
  --out <path>     | Specify an output file for the sitemap. 
  --disguise <url> | Specify a disguise URL for use in the sitemap. Useful when you are creating sitemap for a local website before hosting it.
  

When Running the command, you need to specify the '--url' and the '--out' parameters while the '--disguise' parameter is optional. 
Also, running the command with --version or --help will lead to the suppression of other parameters.""")


def prepare(link:str):
	if(link.endswith("/")):
		link = link[:-1]
	if("http" not in link):
		raise Exception(f"{link} is not a valid URL!")
	return link




