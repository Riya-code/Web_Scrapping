import requests
from bs4 import BeautifulSoup

# url of site from where we to scrap content
url = "https://codewithharry.com"

# Step1: Get the HTML
r = requests.get(url);
htmlContent = r.content
# print(htmlContent)

# Step2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup)
# print(soup.prettify)

# Step3: HTML Tree traversal
#
# Commomly used types of Objects:
# 1.print(type(title)) --> Tag
# 2. print(type(title.string)) --> NavigableString
# 3. print(type(soup)) --> BeautifulSoup
# 4. Comment --> # markup = "<p><!-- this is a comment --></p>"
                 # soup2 = BeautifulSoup(markup)
                 # print(soup2.p)
                 # print(soup2.p.string)
                 # print(type(soup2.p.string))
                 #exit()  # Profram will not run further

# Get the title of html page
title = soup.title
# print(title)

# Getting all para tag
paras = soup.find_all('p')
# print(paras)

# Getting all anchor tag
anchor = soup.find_all('a')
# print(anchor)

# Get first element in html page
#print(soup.find('p'))

# Get classes of any element in the html page
print(soup.find('p')[
          'class'])