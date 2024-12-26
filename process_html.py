
from bs4 import BeautifulSoup
import pandas as pd

def process_magalu_html(file_name='data/test.html', star=0):
    with open(file_name, "r") as file:
        text = file.read()
        soup = BeautifulSoup(text, "lxml")
        text = soup.find_all('span', class_="a-size-base review-text review-text-content")
        
        data = []
        for t in text:
            item = {
                "text": t.findChildren("span" , recursive=False)[0].contents[0],
                "score": star
            }
            data.append(item)
        return data
    
scoreList = []
starsOptions = ["one_star", "two_star", "three_star", "four_star", "five_star"]
starsMap = {
    "one_star": 1, 
    "two_star": 2, 
    "three_star": 3, 
    "four_star": 4, 
    "five_star": 5
}
for opt in starsOptions:
    for pageNumber in range(11):
        try:
            file_name = f"data/page_{opt}_{pageNumber}.html"
            scoreList += (process_magalu_html(file_name, starsMap[opt]))
        except:
            pass

df = pd.DataFrame(scoreList)
df.to_csv("data/dataProcessed.csv")