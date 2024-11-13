from bs4 import BeautifulSoup

import requests

# response = requests.get("https://news.ycombinator.com/news")
response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article in articles:
    article_texts.append(article.getText())
    article_links.append(article.get("href"))
articles_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
# print(article_texts)
# print(article_links)
# print(articles_upvotes)

max_index = articles_upvotes.index(max(articles_upvotes))
print(article_texts[max_index])
print(article_links[max_index])
print(articles_upvotes[max_index])
















# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# # print(soup.title)
#
# all_anchor_tags = soup.find_all(name="a")
#
# #for tag in all_anchor_tags:
#     #print(tag.getText())
#     #print(tag.get("href"))

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)