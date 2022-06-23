from bs4 import BeautifulSoup
# from selenium.webdriver.chrome.options import Options
from selenium import webdriver
# import pickle
# import numpy as np

# def save_cookie(d, path):
#     with open(path, 'wb') as filehandler:
#         pickle.dump(d.get_cookies(), filehandler)

# def load_cookie(d, path):
#     with open(path, 'rb') as cookiesfile:
#         cookiez = pickle.load(cookiesfile)
#         for cookie in cookiez:
#             d.add_cookie(cookie)


def get_url(search_text):
    url = f"https://www.amazon.com/s?k={search_text}&ref=nb_sb_noss_1"
    return url


def extract_asin(single_item):
    try:
        asin = single_item['data-asin']
        # price = price_parent.find("span", "a-offscreen").text
    except AttributeError:
        return
    return asin


def extract_rating(single_item):
    try:
        rating = single_item.find("span", "a-icon-alt").text
    except AttributeError:
        return
    return rating


def extract_record(single_item):
    try:
        price_parent = single_item.find("span", "a-price")
        price = price_parent.find("span", "a-offscreen").text
    except AttributeError:
        return
    return price


def main(search_term, numofpages):
    output = [["ASIN", "Price", "Rating", "Link"]]
    driver = webdriver.Firefox()
    driver.minimize_window()
    driver.get("https://www.amazon.com/")
    load_cookie(driver, "amazon.txt")
    url = get_url(search_term)
    for i in range(numofpages):
        prices = []
        asins = []
        total = 0
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")  # retrieve and parse HTML text.
        url_addition = soup.find(class_="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator").get("href")
        results = soup.find_all("div", {"data-component-type": "s-search-result"})
        for item in results:
            asin = extract_asin(item)
            record = extract_record(item)  # takes each item to extract_record() function above to get the prices
            rating = extract_rating(item)
            if asin:
                asins.append(asin)
                record = str(record).replace(',', '')
                if record == "None":
                    record = 0
                else:
                    record = record[1:]
                rating = str(rating)[0:3]
                prices.append(record)
                link = 'https://www.amazon.com/dp/{}'.format(asin)
                output.append([asin, record, rating, link])
        url = "https://www.amazon.com/" + url_addition

    driver.close()
    return output
