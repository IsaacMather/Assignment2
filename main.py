#methodology:
#lets get a simple web crawler set up to crawl those recommended pages. Once
# we have it set up to return a nice list of those absolute links, and the
# relative links stored as absolute links, we'll then recral each link as an
# iterative function, in a while loop, maybe calling the recursive function
# on each found link?

#regardless, lets get a scrape set up of the first page, and get it
# returning a nice list of links, incluring relative stores as absolute
import requests
from bs4 import BeautifulSoup



def link_fisher(url:  str, depth=0, reg_ex=""):
    link_list = []

    headers = {'User-Agent': ''}

    try:
        page = requests.get(url, headers=headers)
    except:
        print("Cannot access page")
        return link_list
    if page.status_code>=400:
        print("Page Error")

    data = page.text
    # print(data)

    soup = BeautifulSoup(data, features="html.parser")
    for link in soup.find_all('a'):
        link_list.append(link.get("href"))

    print(type(link_list))
    print(link_list)

    # return link_list

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = "http://compsci.mrreed.com"
    url = "http://foothill.edu"
    length = 2
    print(link_fisher(url, length))

