# SitemapGen - Code Documentation

## sitemapgen/\_\_init__.py
The main importng entry point for the library.   



#### `class` Generator
A Class that is used to generate sitemaps from a website's URL and output it as a string or write it to a file.
> `method` **\_\_init__**  
>> The constructer for the class
>>
>> Args:  
>> - **site** (str): The URL of the website to build a sitemap of.  
>> - **output** (str): The path of the output sitemap file.  
>> - **disguise** (str, optional): To set a disguise the sitemap's URL, which is best suited to generate sitemap of a localhost website which needs to be deployed. Defaults to None.    

> `method` **discover**
>> A function to discover all the hyperlinks and the pages available on the domain.
>>
>> Returns:
>> - **list**: A list of all URLs from a website  

> `method` **genSitemap**
>> A function to generate a sitemap and return a copy of the same to the user. Must only be used after `Generator.discover()`
>>
>> Returns:
>> - **str**: The string version of the generated sitemap.  

> `method` **write**
>> Write the sitemap content to the specified output file.

> `method` **getLinks**
>> A function to get the available hyperlinks from the website
>>
>> Args:
>> - **path** (str): The path of the webpage after the domain.
>>
>> Returns:
>> - **list**: All links that could be extracted from the webpage.
		