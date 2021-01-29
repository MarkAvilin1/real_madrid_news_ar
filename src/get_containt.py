from bs4 import BeautifulSoup
import requests


class GetData:
    def __init__(self):
        self.response = requests.get("https://hihi2.com/category/real-madrid-news?utm_source=hihi2&"
                                     "utm_medium=DeskTopLogo&utm_campaign=RealMadrid")
        website_html = self.response.text
        self.soup = BeautifulSoup(website_html, 'html.parser')

        all_titles = self.soup.find_all(name="h2", class_="entry-title")
        self.titles = [title.getText() for title in all_titles]

        all_contents = self.soup.find_all(name="div", class_="entry-excerpt")
        self.contents = [content.getText() for content in all_contents]
        self.all_data = {self.titles[i]: self.contents[i] for i in range(len(self.titles))}
