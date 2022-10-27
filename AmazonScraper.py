from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
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



def get_url(search_text,base):
    url = f"https://{base}/s?k={search_text}&ref=nb_sb_noss_1"
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


def main(search_term, numofpages, base):
    base = 'www.' + base
    try:
        output = [["ASIN", "Price", "Rating", "Link"]]
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.minimize_window()
        driver.get(f"https://{base}/")
        url = get_url(search_term, base)
        for i in range(numofpages):
            prices = []
            asins = []
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, "html.parser")  # retrieve and parse HTML text.
            try:
                url_addition = soup.find(class_="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator").get("href")
            except:
                break
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
                    link = f'https://{base}/dp/{asin}'
                    output.append([asin, record, rating, link])
            url = f"https://{base}/" + url_addition

        driver.close()
        return output
    except:
        driver.close()
        return -1
