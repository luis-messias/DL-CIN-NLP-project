
from bs4 import BeautifulSoup

def process_magalu_html(file_name='data/test.html'):
    with open(file_name, "r") as file:
        text = file.read()
        soup = BeautifulSoup(text, "lxml")
        divs = soup.find_all('div', class_="a-size-base a-color-secondary review-date")
        print(divs[0])

#TODO FIX THIS
for pageNumber in range(1):
    file_name = f"data/page_{pageNumber}.html"
    process_magalu_html(file_name)