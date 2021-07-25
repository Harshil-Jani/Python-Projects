import requests
from bs4 import BeautifulSoup as bs

github_profile = input("Enter the Github UserName : ")
url = f"https://github.com/{github_profile}"
r = requests.get(url)
html_parsing = bs(r.content,'html.parser')
profile_image = html_parsing.find("img",{"alt" : "Avatar"})["src"]
print(profile_image)