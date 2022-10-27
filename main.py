import AmazonScraper2 as AmazonScraper
import csv
import os
import easygui
import datetime

x = datetime.datetime.now()

cur_dir = os.getcwd()

marketplaces = ['United States'
                ,'Canada', 'Mexico', 'United Kingdom', 'France', 'Italy', 'Germany', 'Spain', 'Dutch', 'Sweden', 'Poland', 'Japan', 'Singapore', 'United Arab Emirates', 'Brazil', 'Australia', 'India', 'Saudi Arabia']
marketplaceMapping =    {'United States': 'amazon.com'
                        ,'Canada': 'amazon.ca'
                        ,'Mexico': 'amazon.com.mx'
                        ,'United Kingdom': 'amazon.co.uk'
                        ,'France': 'amazon.fr'
                        ,'Italy': 'amazon.it'
                        ,'Germany': 'amazon.de'
                        ,'Spain': 'amazon.es'
                        ,'Dutch': 'amazon.nl'
                        ,'Sweden': 'amazon.se'
                        ,'Poland': 'amazon.pl'
                        ,'Japan': 'amazon.co.jp'
                        ,'Singapore': 'amazon.sg'
                        ,'United Arab Emirates': 'amazon.ae'
                        ,'Brazil': 'amazon.com.br'
                        ,'Australia': 'amazon.com.au'
                        ,'India': 'amazon.in'
                        ,'Saudi Arabia': 'amazon.sa'}

text = "Enter the following details"
title = "Amazon Scraper"
input_list = ["Search Term", "Pages to search through"]
output = easygui.multenterbox(text, title, input_list, ['', '2'])

text = "Select any one marketplace to scrape."
title = "Marketplace Selection"
output2 = easygui.choicebox(text, title, marketplaces)

searchterm = output[0]
numofpages = int(output[1])
searchterm = searchterm.replace(" ", "+")
a = AmazonScraper.main(searchterm, numofpages, marketplaceMapping[output2])
while a == -1:
    message = "An error has occured. Please make sure that the marketplace link is correctly formatted.\nAlso make sure the other inputs are correctly typed."
    title = "Error"
    ok_btn_txt = "OK"
    output = easygui.msgbox(message, title, ok_btn_txt)

    text = "Enter the following details"
    title = "Amazon Scraper"
    input_list = ["Search Term", "Pages to search through"]
    output = easygui.multenterbox(text, title, input_list, ['', '2'])

    text = "Select any one marketplace to scrape."
    title = "Marketplace Selection"
    output2 = easygui.choicebox(text, title, marketplaces)

    searchterm = output[0]
    numofpages = int(output[1])
    searchterm = searchterm.replace(" ", "+")
    a = AmazonScraper.main(searchterm, numofpages, marketplaceMapping[output2])

b = r'\\'
init_path = cur_dir + '\output' + b[0] + searchterm.replace('+', '_') + ' ' + marketplaceMapping[output2].replace('.','_') + ' ' + str(x)[:19].replace(':', '') + '.csv'

try:
    file = open(init_path, 'w', newline='')
except:
    os.mkdir(cur_dir + '\output')
    file = open(init_path, 'w', newline='')
with file:
    write = csv.writer(file)
    write.writerows(a)
