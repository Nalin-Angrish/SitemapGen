# SitemapGen
### A Command line tool to let you easily create XML sitemaps from a website's URL

## Installing
1. **PIP:**  run  ``` pip install sitemapgen ```
2. **Without PIP:** 
	1. Clone this repository by running:  
	```git clone https://github.com/Nalin-2005/SitemapGen.git```  
	Or download it as ZIP.
	2. `cd` into the downloaded directory by ```cd SitemapGen```.
	3. Run ```python setup.py install```.

## Usage
### CLI
1. After you have installed the library, fire up a Terminal/Command Prompt and type ```sitemapgen --help```. This command will show you the description of the library and the available options for using the command.   
```
SitemapGen v0.9.5 - By Nalin Angrish.
A general utility script for generating site XML sitemaps.  

Options:  
--version        | Show the tool version  
--help           | Show this message and exit.  
--url <url>      | Specify a website url to generate a sitemap from.   
--out <path>     | Specify an output file for the sitemap.   
--disguise <url> | Specify a disguise URL for use in the sitemap. Useful when you are creating sitemap for a local website before hosting it.  
     
  
When Running the command, you need to specify the '--url' and the '--out' parameters while the '--disguise' parameter is optional.   
Also, running the command with --version or --help will lead to the suppression of other parameters.  
```
2. To know the version of the tool, run ```sitemapgen --version```   
```
SitemapGen v0.9.5 - By Nalin Angrish.
```
3. To create a sitemap for a website, run ```sitemapgen --url <URL of website> --out <Path to output sitemap>```. The URL specified here should not be blocked by a firewall and should be a complete URL. For example: `localhost` would not be valid and you would have to use `http://localhost`. If the output file specified does not exists, then it will be created. You can specify the output path as either a relative path to the current working directory or even an absolute path.
4. Sometimes, when you create a sitemap for a website in development, you need to use a different domain in the sitemaps than the development domain. For example, while developing, the `--url` would be specified as `http://localhost:port` whereas, in the sitemap you might need to use a domain like `http://www.example.com`. In such cases, you can provide another option to the command line arguments by adding: 
``` --disguise http://www.example.com ```. It is always prefered to use `http` instead of `https` to avoid any future issue with the SSL certificate installation. So, the tool will automatically use the ```http``` versions of the sites

### Programatically
 The library provides a `Generator` class that can be used to generate a sitemap of a given URL. This is an example of how to use the `Generator` class:
 ```
 from sitemapgen import Generator          # Import the Generator class


generator = Generator(site="http://localhost", output="sitemap.xml", disguise="http://www.example.com") 		# Create a generator instance where:
				# site = The site to generate a sitemap of. (required)
				# output = The path of the output file. (required) If the sitemap is not be written to a file, just set it to an empty string.
				# disguise = The url to disguise the sitemap for. (optional) 

urls = generator.discover()        # Discover all URLs possible from the "site" specified during initialization. 
				# This function returns the URLs discovered but it's return value can also be ignored if the urls don't matter 
				# (If they are ultimately going to be written to a file)
				# Returns a list

sitemap = generator.genSitemap()   # Generate a String sitemap from the URLs discovered before. Should only be used after calling generator.discover()
				# This function returns the generated sitemap but it's return value can also be ignored if the sitemap is just to be written to a file.
				# Returns a String

generator.write()      # Write to the output file specified. No return value.
 ```  
  
 To read the code documentation, go [here](http://nalin-2005.github.io/SitemapGen/)