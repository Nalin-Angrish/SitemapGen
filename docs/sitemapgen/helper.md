# SitemapGen - Code Documentation

## sitemapgen/helper.py
A python file that contains some helper methods for the working of the library/tool. 


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

#### `method` rectify
> A function to check a link and verify that it should be captured or not. For e.g. any external URL would be blocked. It would also take care that all the urls are properly formatted.
>
>
> Args:
> - **link (str)**: the link to rectify.
> -	**parent (str)**: the complete url of the page from which the link was found.
> -	**path (str)**: the path (after the domain) of the page from which the link was found.
>
>Returns:
> -	**str**: the properly formatted link.