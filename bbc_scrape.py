import requests
from bs4 import BeautifulSoup as bs

class BBC:
    def __init__(self, url:str):
        article = requests.get(url)
        self.soup = bs(article.content, "html.parser")
        self.body = self.get_body()
        self.title = self.get_title()
        self.body_search  = self.body_search()
        
    def get_body(self) -> list:
        body = self.soup.find("article")
        return [p.text for p in body.find_all("p", class_="ssrcss-1q0x1qg-Paragraph eq5iqo00")]
    
    def body_search(self) -> list:
        text_blocks = self.soup.find_all('div', {'data-component': 'text-block'})
        result = []
        for text_block in text_blocks:
            paragraphs = text_block.find_all('p')
            for p in paragraphs:
                result.append(p.get_text())
        return result
    
    
    def get_title(self) -> str:
        return self.soup.find("h1").text

#print(BBC("https://www.bbc.co.uk/news/world-europe-49345912").body)
print(BBC("https://www.bbc.co.uk/news/world-europe-49345912").body_search)
print(BBC("https://www.bbc.co.uk/news/world-europe-49345912").title)
#https://www.bbc.co.uk/news/world-europe-49345912