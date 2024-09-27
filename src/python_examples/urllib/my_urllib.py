"""This module is an example of how to use urllib to download a file from the internet."""

from urllib import parse

url = "https://www.w3.org/WAI/ER/tests/xhtmltestfiles/resour ces/pdf/dummy.pdf"
encoded_url = parse.quote(url, safe=":/")
print(f"URL: {url}")
print(f"Encoded URL: {encoded_url}")
print(f"URL Parse Result: {parse.urlparse(url)}")
print(f"Parsed URL: {parse.urlparse(url)}")


# filename = "dummy.pdf"
# urllib.request.urlretrieve(url, filename)
# print(f"Downloaded {filename} from {url}")


#urlencode
print("urlencode:",parse.urlencode({"key": "value with spaces"}))



########## How to prepare right github search url #############
from urllib.parse import urlencode

repo="example-repo"
value = "Something to search"
query = f'repo:Company/{repo} "{value}"'
params = {"q": query, "type": "code"}
encoded_params = urlencode(params)

url = f"https://github.com/search?{encoded_params}"
print(url)
# output:
# https://github.com/search?q=repo%3ACompany%2Fexample-repo+%22Something+to+search%22&type=code
