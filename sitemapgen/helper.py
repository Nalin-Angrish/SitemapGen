"""
A python file that contains some helper methods for the working of the library/tool.
"""
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






def displayHelpMessage(VERSION):
	"""A function to display a help message to the user
	
	Args:
		**VERSION** (str): The version of the library.
	"""
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
	"""A function to check if the link is complete (it includes the protocol) 
	and that it can be used by the library (it should not end with a slash)


	Args:
		**link (str)**: The link to check/prepare

	Raises:
		**Exception**: Thrown if the protocol is not present in the URL 

	Returns:
		**str**: prepared link
	"""
	if(link.endswith("/")):
		link = link[:-1]
	if("http" not in link):
		raise Exception(f"{link} is not a valid URL!")
	return link



def rectify(link:str, parent:str, path:str):
	"""A function to check a link and verify that it should be captured or not.
	For e.g. any external URL would be blocked. It would also take care that all the urls are properly formatted.

	Args:
		**link (str)**: the link to rectify.
		**parent (str)**: the complete url of the page from which the link was found.
		**path (str)**: the path (after the domain) of the page from which the link was found.

	Returns:
		**str**: the properly formatted link.
	"""
	if (link.startswith("#")) or (":" in link) or ("../" in link):
		return path
	if not link.startswith("/"):
		if parent.endswith("/"):
			if not path.endswith("/"):
				path += "/"
			return path + link
		else:
			path = "/".join(path.split("/")[:-1])+"/"
			return path + link

	return link
