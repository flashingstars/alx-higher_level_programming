This directory contains tasks that show us how to fetch internet resources with python package urllib, decode urllib response, use python package requests, make http GET, POST and PUT requests, fetch JSON resource and manipulate data from an external service.

0. A script that fetches https://alx-intranet.hbtn.io/status
	Use package urllib package only using with statement 

1. A python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.
	Use the package urllib and sys only and with statement

2. A script that takes in a URL and an email, sends a POST request to the URL with the email as a parameter and displays the body of the response decoded in utf-8
	Email must be sent in the email variable
	Use packages urllib and sys only
	Use with statement

3. A script that takes a URL, sends a request to the URL and displays the body of the response decoded wuth UTF-8
	Manage urllib.error.HTTPerror exceptions and print:Error code: with the HTTP status code
	import urllib and sys only
	Use with statement

4. A script that fetches https://alx-intranet.hbtn.io/status
	Use requests package only

5. A script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header
	Use the packages requests and sys only
	The value of the variable is different with each request

6. A script that takes a URL and email address, sends a POST request to the passed URL with the email as a parameter and finally displays the body of the response
	The email must be sent in the variable email
	Use the packages requests and sys only

7. A script that takes in a URL, sends a request to the URL and displays the body of the response
	If the HTTP status is greater than or equal to 400, print:Error code: and the value of the HTTP status code
	Use requests and sys packages only

8. A script that takes a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter
	The letter must be sent in the variable q
	If no argument is given, set q=""
	If the response body is properly JSON formatted and not empty, display the id and name like this [<id>] <name>, otherwise
		Display Not a valid JSON if the JSON is invalid
		Display No result if the JSON is empty
	Use the packages requests and sys only

9. A script that takes my Github credentials (username and password) and uses the Github API to display my id
	Use Basic Authentication with a personal access token as password to access my information (only read:user permission is needed)
	First argument will be my username
	Second argument will be my password
	Use the packages requests and sys only
