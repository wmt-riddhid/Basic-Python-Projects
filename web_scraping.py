# This is a web scraping python project in which have to ask for user input for a GitHub user link and output the profile image link through web scraping. 
# Web scraping is a technique that collects data from a web page. 

import profile
import requests
from bs4 import BeautifulSoup as bs

github_user = input("Input github user : ")
url = "https://github.com/" + github_user
r = requests.get(url)
soup = bs(r.content, "html.parser")
profile_image = soup.find("img", {"alt":"Avatar"})["src"]
print(profile_image)