"""
The file containing the main CLI code. 
"""
from . import *
from sys import argv
import re, time



def run():
	"""The main function that runs the CLI code.
	The CLI Supports the following options:
	-  --version        | Show the tool version
  	-  --help           | Show this message and exit.
  	-  --url <url>      | Specify a website url to generate a sitemap from. 
    -  --out <path>     | Specify an output file for the sitemap. 
    -  --disguise <url> | Specify a disguise URL for use in the sitemap. Useful when you are creating sitemap for a local website before hosting it.
	"""
	if("--version" in argv):
		print(f"SitemapGen {VERSION} - By Nalin Angrish.")
		exit(0)

	if("--help" in argv):
		displayHelpMessage(VERSION)
		exit(0)

		

	try:
		site = prepare(argv[argv.index("--url")+1])
		disguise = site
		if("--disguise" in argv):
			disguise = prepare(argv[argv.index("--disguise")+1])
		output = argv[argv.index("--out")+1]
	except ValueError as e:
		errorkey = re.findall("'.*'", str(e))[0]
		print("Cannot find a required parameter: " + errorkey + ". Use \"sitemapgen --help\" for more information about how to use the command")
		exit(1)

	print("Generating sitemap for URL: \""+site+"\"")
	if(disguise!=site):
		print("Disguising all URLs to the domain: \""+disguise+"\"")
	print("The output File is present/would be created at: \""+output+"\"")

	time.sleep(2)

	generator = Generator(site, output, disguise)

	print("Discovering URLs.....")
	urls = generator.discover()
	print(f"Discovered {str(len(urls))} URLs.....")
	time.sleep(2)

	print("Generating sitemap.....")
	sitemap = generator.genSitemap()
	time.sleep(2)
	print("Sitemap Generated.....")

	print("Writing Sitemap to output file.....")
	generator.write()
	time.sleep(2)
	print("Sitemap successfully written.....")