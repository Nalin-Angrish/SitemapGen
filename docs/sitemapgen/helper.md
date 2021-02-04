# SitemapGen - Code Documentation

## sitemapgen/helper.py
A python file that contains some helper methods for the working of the library/tool. 

#### `method` filter
>A function to remove the duplicates in a list so that no URL is repeated in the sitemap.
>	This function also checks if the links are on the same domain or not and if they are linked to an external website, then the URL is removed.  
>
> Args:
> - **array** (list): The list to filter
>
> Returns:
> - **list**: a filtered list

#### `method` displayHelpMessage
> A function to display a help message to the user.
>	
> Args:  
> - **VERSION** (str): The version of the library.

#### `method` prepare
> A function to check if the link is complete (it includes the protocol) and that it can be used by the library (it should not end with a slash)
>
>
> Args:
> - **link** (str): The link to check/prepare
>
> Raises:
> - **Exception**: Thrown if the protocol is not present in the URL 
>
> Returns:
> - **str**: prepared link