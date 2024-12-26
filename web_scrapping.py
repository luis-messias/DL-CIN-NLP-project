from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os.path
import time

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

driver.get("https://www.amazon.com.br/Apple-iPhone-15-128-GB/product-reviews/B0CP6CVJSG/ref=cm_cr_getr_d_paging_btm_next_3?ie=UTF8&reviewerType=all_reviews&pageNumber=3")
time.sleep(60)

def save_html_on_file(search_url, file_name='data/test.html'):
    driver.get(search_url)
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
    divs = soup.find_all('div', class_="a-size-base a-color-secondary review-date")

    print(divs[0])
    if len(divs) < 1:
        return False
    
    with open(file_name, "w") as f:
        f.write(html)

    return True

pageNumber = 0
retry = 0
maxRetry = 10

while True:
    if retry > maxRetry:
        print(f"Max Retry. Last page: {pageNumber}. Retry count {retry}")
        break

    search_url = f"https://www.amazon.com.br/Apple-iPhone-15-128-GB/product-reviews/B0CP6CVJSG/ref=cm_cr_getr_d_paging_btm_next_{pageNumber}?ie=UTF8&reviewerType=all_reviews&pageNumber={pageNumber}"
    # search_url = f"https://www.magazineluiza.com.br/review/220559300/jogo-de-toalhas-de-banho-atlantica-delicata-garden-gengibre-4-pecas/CM/JOTO/?page={pageNumber}&sortType=MOST_RECENT"
    file_name = f"data/page_{pageNumber}.html"

    if os.path.isfile(file_name):
        print(f"Page {pageNumber} already get, skipping")
        retry = 0
        pageNumber += 1
        continue

    try:
        divs_found = save_html_on_file(search_url, file_name)
    except:
        print(f"Something fail on page number {pageNumber}. Reloading and retrying.")

        # options = Options()
        # options.headless = True
        # driver = webdriver.Chrome(options=options)
        retry += 1
        time.sleep(1)
        continue

    if divs_found:
        print(f"Review found, page number {pageNumber}")
        retry = 0
        pageNumber += 1
        time.sleep(1)
    else:
        retry += 1
        print(f"Review not found. Retrying page number {pageNumber}, retry count {retry}")

while True:
    pass