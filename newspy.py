# scrape all news article titles from main page of bbc into a plain note to read later
import datetime

import requests, bs4

url = "https://www.bbc.co.uk/news"

res = requests.get(url)
soup = bs4.BeautifulSoup(res.text, "html.parser")
articleElem = soup.select("div[type='article'] a[href]")
with open("today's headlines.txt", "at", encoding="utf-8") as note:
    note.write("~."*20+str(datetime.date.today())+"~."*20+"\n")
    for i in range(0, len(articleElem)):
        note.write("\n"+articleElem[i].text)
    note.write("\n\n")